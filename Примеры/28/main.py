from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template(
        'index.html',
        text='<h1>Заголовок1</h1>'
    )
