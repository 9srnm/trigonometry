themes = [
    {
        'name': "Табличные углы",
        'shortname': "table",
        'description': "В этой теме рассказывается о значениях т/г функций табличных углов",
        'text':
"""Табличные значения тригонометрических функций можно определить по тригонометру:
image:unit_circle.png
Четность и нечетность т/г функций:
\(\sin{(-x)}=-\sin{x}\) — нечетная функция
\(\cos{(-x)}=\cos{x}\) — четная функция
\(tg(-x)=-tgx\) — нечетная функция
\(ctg(-x)=-ctgx\) — нечетная функция
Целое число полных оборотов НЕ МЕНЯЕТ ЗНАЧЕНИЕ функции""",
        'tasks': [
            {
                'text': "Найдите значение выражения: \[2\cos60^\circ+\sqrt{3}\cos30^\circ\]",
                'answer': 2.5
            },
            {
                'text': "Найдите значение выражения: \[2\sin30^\circ+6\cos60^\circ-4tg45^\circ\]",
                'answer': 0
            },
            {
                'text': "Найдите значение выражения: \[tg360^\circ-{3 \over 4}\sin270^\circ-{1 \over 4}\cos180^\circ\]",
                'answer': 1
            },
            {
                'text': "Найдите значение выражения: \[\sin330^\circ+\sin0^\circ+2\cos60^\circ\]",
                'answer': 0.5
            },
            {
                'text': "Найдите значение выражения: \[tg(-900^\circ)+\cos720^\circ+2\cos0^\circ-4\sin90^\circ+5tg180^\circ\]",
                'answer': -1
            },
        ]
    },
    {
        'name': "Основные тождества",
        'shortname': "main",
        'description': "В этой теме рассказывается о радианной мере угла и основных т/г тождествах",
        'text':
"""\(l={\pi \over 180^\circ} * \gamma\) — перевод градусов в радианы
\(\gamma={l \over \pi} * 180^\circ\) — перевод радиан в градусы
Основное тригонометрическое тожедество (ОТТ): \[\sin^2x+\cos^2x=1\]
\(tg x={\sin x \over \cos x}, \cos x \\neq 0\)
\(ctg x={\cos x \over \sin x}={1 \over tg x}, \sin x \\neq 0\)
\(tg x * ctg x = 1\)
\(tg^2x + 1 = {1 \over \cos^2 x}; ctg^2x + 1 = {1 \over \sin^2 x}\)""",
        'tasks': [
            {
                'text': "Найдите значение выражения: \[3-\sin^2{\pi \over 3}+2\cos^2{\pi \over 2}-5tg^2{\pi \over 4}\]",
                'answer': -2.25
            },
            {
                'text': "Найдите значение выражения: \[5\sin{\pi \over 4}+3tg{\pi \over 4}-5\cos{\pi \over 4}-10ctg{\pi \over 4}\]",
                'answer': -7
            },
            {
                'text': "Найдите значение выражения: \[{1 - tg(-x) \over \sin x + \cos(-x)}\] при \(\cos x=2\)",
                'answer': 0.5
            },
            {
                'text': "Найдите значение выражения: \[{\sin^2x-\cos^2x+1 \over \sin^2x}\]",
                'answer': 0
            },
        ]
    },
    {
        'name': "Формулы приведения",
        'shortname': "reduction",
        'description': "В этой теме рассказывается о формулах приведения и «лошадином правиле»",
        'text':
"""\(\sin(90^\circ-\gamma)=\cos\gamma; \sin(180^\circ-\gamma)=\sin\gamma; \sin(270^\circ-\gamma)=-\cos\gamma; \sin(360^\circ-\gamma)=-\sin\gamma\)
    \(\cos(90^\circ-\gamma)=\sin\gamma; \cos(180^\circ-\gamma)=-\cos\gamma; \cos(270^\circ-\gamma)=-\sin\gamma; \cos(360^\circ-\gamma)=\cos\gamma\)
    \(tg(90^\circ-\gamma)=ctg\gamma; tg(180^\circ-\gamma)=-tg\gamma; tg(270^\circ-\gamma)=ctg\gamma; tg(360^\circ-\gamma)=-tg\gamma\)
    \(ctg(90^\circ-\gamma)=tg\gamma; ctg(180^\circ-\gamma)=-ctg\gamma; ctg(270^\circ-\gamma)=tg\gamma; ctg(360^\circ-\gamma)=-ctg\gamma\)

    \(\sin(90^\circ+\gamma)=\cos\gamma; \sin(180^\circ+\gamma)=-\sin\gamma; \sin(270^\circ+\gamma)=-\cos\gamma; \sin(360^\circ+\gamma)=\sin\gamma\)
    \(\cos(90^\circ+\gamma)=-\sin\gamma; \cos(180^\circ+\gamma)=-\cos\gamma; \cos(270^\circ+\gamma)=\sin\gamma; \cos(360^\circ+\gamma)=\cos\gamma\)
    \(tg(90^\circ+\gamma)=-ctg\gamma; tg(180^\circ+\gamma)=tg\gamma; tg(270^\circ+\gamma)=-ctg\gamma; tg(360^\circ+\gamma)=tg\gamma\)
    \(ctg(90^\circ+\gamma)=-tg\gamma; ctg(180^\circ+\gamma)=ctg\gamma; ctg(270^\circ+\gamma)=-tg\gamma; ctg(360^\circ+\gamma)=ctg\gamma\)

    «Лошадиное правило»
    \(f({\pi \over 2} k \pm \gamma), k = 2n - 1, n \in N\) — смена функции
    \(g(\pi k \pm \gamma)\) — нет смены функции
    Знак новой функции (правой части) определяется по знаку исходной ф-ции (левой части)""",
        'tasks': [
            {
                'text': "Найдите значение выражения: \[{ctg({\pi \over 2} + \gamma) - tg(\pi + \gamma) + sin({3\pi \over 2} - \gamma) \over \cos(\pi + \gamma)}\]",
                'answer': 1
            },
            {
                'text': "Найдите значение выражения: \[\sin(\pi - x) * \cos({\pi \over 2} - x) - \sin({\pi \over 2} + x) * \cos(\pi - x)\]",
                'answer': 1
            },
            {
                'text': "Найдите значение выражения: \[{\sin({3\pi \over 2} + \gamma) \over ctg(2\pi - \gamma)}*{tg({\pi \over 2} + \gamma) \over \sin(\pi + \gamma) * ctg \gamma} + 2\]",
                'answer': 3
            },
            {
                'text': "Найдите значение выражения: \[{\sin(\pi - \gamma) + \cos({\pi \over 2} + \gamma) + ctg(\pi - \gamma) \over tg({3\pi \over 2} - \gamma)}\]",
                'answer': -1
            },
            {
                'text': "Найдите значение выражения: \[{4\sin(\pi - \gamma) \over tg(\pi + \gamma)} * {ctg({\pi \over 2} - \gamma) \over tg({\pi \over 2} + \gamma)} * {\cos(2\pi - \gamma) \over \sin(-\gamma) * \sin\gamma}\]",
                'answer': 4
            },
        ]
    },
    {
        'name': "Формулы сложения",
        'shortname': "addition",
        'description': "В этой теме рассказывается о формулах сложения т/г функций",
        'text':
"""Формула суммы/разности синусов: \(\sin(x \pm y) = \sin x \cos y \pm \cos x \sin y\)
Формула суммы/разности косинусов: \(\cos(x \pm y) = \cos x \cos y \mp \sin x \sin y\)
Формула суммы/разности тангенсов: \(tg(x \pm y) = {tgx \pm tgy \over 1 \mp tgx tgy}\)""",
        'tasks': [
            {
                'text': "Найти \[85\cos(x + y)\] при \(\sin x = -{3 \over 5} ({3\pi \over 2} \lt x \lt 2\pi), \sin y = {8 \over 17} (0 \lt y \lt {\pi \over 2})\)",
                'answer': 36
            },
            {
                'text': "Найти \[85\cos(x - y)\] при \(\sin x = -{3 \over 5} ({3\pi \over 2} \lt x \lt 2\pi), \sin y = {8 \over 17} (0 \lt y \lt {\pi \over 2})\)",
                'answer': 84
            },
            {
                'text': "Чему равен \(\cos 3x\) \[-\sin({3\pi \over 2} - 5x)\cos(2x + 4\pi) - \sin(5x + \pi)\sin 2x = 0\]",
                'answer': 0
            },
            {
                'text': "Найти значение через формулы сложения: \[{\cos({3\pi \over 2} + x) \over \sin x}\]",
                'answer': 1
            },
            {
                'text': "Найти значение через формулы сложения: \[{\cos(\pi - x) \over \cos x}\]",
                'answer': -1
            },
        ]
    },
    {
        'name': "Формулы двойного угла",
        'shortname': "double",
        'description': "В этой теме рассказывается о формулах двойного угла",
        'text':
"""Синус двойного угла: \(\sin 2x = 2\sin x \cos x\)
Косинус двойного угла: \(\cos 2x = \cos^2x - \sin^2x = 2\cos^2x - 1 = 1 - 2\sin^2x\)
Тангенс двойного угла: \(tg2x = {2tgx \over 1 - tg^2x}\)""",
        'tasks': [
            {
                'text': "Найдите значение выражения: \[(\cos 75^\circ - \sin 75^\circ)^2\]",
                'answer': 0.5
            },
            {
                'text': "Найдите значение выражения: \[{1+\cos^2x-\sin^2x \over 1-\cos^2x+\sin^2x}\] при \(ctgx=2\)",
                'answer': 4
            },
            {
                'text': "Найдите значение выражения: \[4\sin{x \over 2}\sin{\pi - x \over 2}\sin({3\pi \over 2} - x) + \cos x\]",
                'answer': 1
            },
            {
                'text': "Найдите значение выражения: \[{2\sin^2x-1-4\cos^2x\sin^2x+2\cos^2x \over 4\sin^2x\cos^2x}\] при \(ctg2x = 1.5\)",
                'answer': 2.25
            },
        ]
    },
]