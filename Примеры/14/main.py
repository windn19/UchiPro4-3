from flask import Flask, render_template

app = Flask(__name__)

context = {'title': 'Заголовок',
           'text': 'Текст'}


@app.route('/')
def index():
    return render_template(
        'index.html',
        context=context,
    )
