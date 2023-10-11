from os import getenv
from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from flask_migrate import Migrate

from app.config import enviroment

app = Flask(__name__)

app.config.from_object(enviroment[getenv('FLASK_ENV')])

api = Api(
    app,
    title='Mi primer app en Flask',
    description='Endpoints de mi primer app en Flask',
    version='1.1',
    doc='/swagger-ui'
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
