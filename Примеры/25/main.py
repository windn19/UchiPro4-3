from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<int:n>')
def index(n):
    return render_template(
        'index.html',
        n=n
    )
