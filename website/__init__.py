from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
#from flask_login import LoginManager

db = SQLAlchemy()
print('runs')
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}.db'
    app.config['SECRET_KEY'] = 'some-other-secret-key'


    from .views import views
    #from .auth import auth

    app.register_blueprint(views, url_prefix='/')


    return app