from flask import Flask
from views.index import my_app
# from flask import Blueprint, request, render_template, redirect, url_for
from werkzeug.exceptions import NotFound, BadRequest

app = Flask(__name__)
app.register_blueprint(my_app, url_prefix='/')

# @app.route("/")
# def root():
#     return "Hello World!!"


# @app.route("/about/")
# def about():
#     return "about me"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
