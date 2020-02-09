import os

from flask import Flask

# Set log message level tensorflow
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # For authentication
    SECRET_KEY = os.urandom(32)
    app.config['SECRET_KEY'] = SECRET_KEY

    from application.routes import ml_app

    app.register_blueprint(ml_app)

    return app
