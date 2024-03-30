from flask import Flask, render_template

app = Flask(__name__)

lst = ['кошка', 'мышка', 'собака']


@app.route('/')
def index():
    return render_template(
        'index.html',
        lst=lst
    )
