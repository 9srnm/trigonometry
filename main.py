from config import *
from text import *
from flask import Flask, render_template, request, redirect
from sqlalchemy.sql import func
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{DB["username"]}:{DB["password"]}@{DB["host"]}/{DB["name"]}'


from models import *


def set_data(db):
    existing_themes = [i.name for i in Themes.query.all()]
    for theme in themes:
        if theme['name'] not in existing_themes:
            new_theme = Themes(name=theme['name'], shortname=theme['shortname'], description=theme['description'], text=theme['text'])
            db.session.add(new_theme)
            db.session.commit()

            theme_id = Themes.query.where(Themes.name == theme['name']).one().id
            for task in theme['tasks']:
                new_task = Tasks(theme=theme_id, text=task['text'], answer=task['answer'])
                db.session.add(new_task)
            db.session.commit()

            new_variant = Variants(is_theme=True, theme=theme_id)
            db.session.add(new_variant)
            db.session.commit()

            variant_id = Variants.query.where(Variants.theme == theme_id).one().id
            tasks = Tasks.query.where(Tasks.theme == theme_id).order_by(Tasks.id)
            for i, task in enumerate(tasks):
                task_in_var = TasksInVariants(task=task.id, variant=variant_id, position=i + 1)
                db.session.add(task_in_var)
            db.session.commit()


with app.app_context():
    db.create_all()
    set_data(db)


@app.route('/')
def index():
    existing_themes = Themes.query.all()
    error = request.args.get('error', type=int)
    return render_template("index.html", themes=existing_themes, error=error)


@app.route('/themes')
def themes():
    existing_themes = Themes.query.all()
    return render_template("themes.html", themes=existing_themes)


@app.route('/themes/<theme_name>')
def theme(theme_name):
    this_theme = Themes.query.where(Themes.shortname == theme_name).one()
    variant = Variants.query.where(Variants.theme == this_theme.id).one()
    tasks_in_variant = TasksInVariants.query.where(TasksInVariants.variant == variant.id).order_by(TasksInVariants.position).all()
    tasks = [Tasks.query.where(Tasks.id == task.task).one() for task in tasks_in_variant]
    return render_template("theme.html", theme=this_theme, tasks=tasks)


@app.route('/tasks')
def tasks():
    existing_tasks = Tasks.query.all()
    tasks = []
    for task in existing_tasks:
        tasks.append({'theme': Themes.query.where(Themes.id == task.theme).one().name, 'text': task.text, 'answer': task.answer})
    return render_template("tasks.html", tasks=tasks)


@app.route('/get_variant')
def get_variant():
    args_themes = list(request.args.keys())
    themes = Themes.query.all()
    themes_names = [theme.shortname for theme in themes]
    themes_ids = [theme.id for theme in themes]
    num_tasks_for_theme = {}
    for theme in args_themes:
        try:
            ind = themes_names.index(theme)
        except ValueError:
            ind = -1
        if ind != -1:
            if request.args[theme] != 0:
                num_tasks_for_theme[themes_ids[ind]] = request.args[theme]

    tasks = []
    for theme in num_tasks_for_theme.keys():
        tasks_for_theme = Tasks.query.where(Tasks.theme == theme).order_by(func.rand()).limit(num_tasks_for_theme[theme]).all()
        tasks += tasks_for_theme

    if len(tasks) == 0:
        return redirect('/?error=1')

    random.shuffle(tasks)
    tasks_ids = [task.id for task in tasks]

    tasks_variants = []
    min_len = 1e9
    ind = 0
    for i, task_id in enumerate(tasks_ids):
        variants = TasksInVariants.query.where(TasksInVariants.task == task_id, TasksInVariants.position == i + 1).all()
        tasks_variants.append([variant.variant for variant in variants])
        if len(variants) < min_len:
            min_len = len(variants)
            ind = i

    found_variant = -1

    for variant in tasks_variants[ind]:
        for variants in tasks_variants:
            if variant not in variants:
                break
        else:
            found_variant = variant
            break

    if found_variant == -1:
        variant = Variants(is_theme=False)
        db.session.add(variant)
        db.session.commit()
        variant = Variants.query.order_by(Variants.id.desc()).first()
        for i, task_id in enumerate(tasks_ids):
            task = TasksInVariants(task=task_id, variant=variant.id, position=i + 1)
            db.session.add(task)
        db.session.commit()

    variant_number = found_variant if found_variant != -1 else variant.id
    return redirect(f'/variant/{variant_number}')


@app.route('/variant/<variant_number>')
def variant(variant_number):
    tasks = [Tasks.query.where(Tasks.id == task.task).one() for task in TasksInVariants.query.where(TasksInVariants.variant == variant_number).order_by(TasksInVariants.position).all()]
    return render_template("variant.html", variant=variant_number, tasks=tasks)


@app.route('/result', methods=['POST'])
def result():
    variant_number = request.form.get('variant', type=int)
    if not variant_number:
        return redirect('/?error=1')
    tasks_nums = list(request.form.keys())
    tasks_nums.remove('variant')
    tasks_nums.sort(key=lambda x: int(x))
    tasks = [Tasks.query.where(Tasks.id == task.task).one() for task in TasksInVariants.query.where(TasksInVariants.variant == variant_number).order_by(TasksInVariants.position).all()]
    answers = [{'result': request.form.get(task, type=str), 'correct': request.form.get(task, type=str) and request.form.get(task, type=str).replace(',', '.').count('.') <= 1 and (request.form.get(task, type=str)[0] == '-' and len(request.form.get(task, type=str)) >= 2 and ''.join(request.form.get(task, type=str)[1:].replace(',', '.').split('.')).isdigit() or request.form.get(task, type=str)[0] != '-' and ''.join(request.form.get(task, type=str).replace(',', '.').split('.')).isdigit()) and float(request.form.get(task, type=str).replace(',', '.')) == tasks[i].answer} for i, task in enumerate(tasks_nums)]
    return render_template("result.html", variant=variant_number, tasks=tasks, answers=answers)