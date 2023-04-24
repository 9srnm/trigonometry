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
]