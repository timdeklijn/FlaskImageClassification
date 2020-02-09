import os

from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(".", ".flaskenv"))


class Config:
    FLASK_APP = os.getenv("FLASK_APP")
    FLASK_ENV = os.getenv("FLASK_ENV")
    FLASK_RUN_POST = os.getenv("FLASK_RUN_PORT")
