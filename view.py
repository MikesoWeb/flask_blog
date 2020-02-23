from app import app
from flask import render_template

name = 'Mike'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/blog')
def blog():
    return render_template("blog.html")


@app.route('/plan')
def plan():
    return render_template("plan.html")
