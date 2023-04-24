from config import *
from text import *
from flask import Flask, render_template

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

with app.app_context():
    db.create_all()
    set_data(db)


@app.route('/')
def index():
    existing_themes = Themes.query.all()
    return render_template("index.html", themes=existing_themes)


@app.route('/themes')
def themes():
    existing_themes = Themes.query.all()
    return render_template("themes.html", themes=existing_themes)


@app.route('/tasks')
def tasks():
    existing_tasks = Tasks.query.all()
    tasks = []
    for task in existing_tasks:
        tasks.append({'theme': Themes.query.where(Themes.id == task.theme).one().name, 'text': task.text, 'answer': task.answer if int(task.answer) != task.answer else int(task.answer)})
    return render_template("tasks.html", tasks=tasks)