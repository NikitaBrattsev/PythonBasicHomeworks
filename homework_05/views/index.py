from flask import Blueprint
from flask.templating import render_template

my_app = Blueprint("my_app", __name__)


@my_app.route("/", endpoint="index")
def get_index():
    return render_template('index.html')


@my_app.route("/about/", endpoint="about")
def get_about():
    return render_template('about.html')
