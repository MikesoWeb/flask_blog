from flask import render_template, Flask

from .config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)


@app.route('/')
def index():
    return render_template("blog/index.html")


@app.get('/blog')
def get_blog():
    return render_template("blog/blog.html")


@app.get('/plan')
def get_plan():
    return render_template("blog/plan.html")
