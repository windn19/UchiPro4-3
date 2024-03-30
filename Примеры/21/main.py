from flask import Flask, render_template

app = Flask(__name__)

context = {'Заголовок 1': 'Текст 1',
           'Заголовок 2': 'Текст 2',
           'Заголовок 3': 'Текст 3'}


@app.route('/')
def index():
    return render_template(
        'index.html',
        context=context,
    )
