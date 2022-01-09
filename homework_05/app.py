from flask import Flask
from views.index import my_app


app = Flask(__name__)
app.register_blueprint(my_app, url_prefix='/')


if __name__ == "__main__":
    app.run(host='0.0.0.0')
