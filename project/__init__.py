from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "todo.db"

def create_app():
    app = Flask(__name__)    
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config['SECRET_KEY'] = 'c73102896e4e74edcb824dcb'
    db.init_app(app)


    from .app import view
    from .auth import auth
    app.register_blueprint(view, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    #creates database if already do not exist
    from .models import User,Todo
    create_db(app)

    login_manager = LoginManager()
    login_manager.login_view='auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_db(app):
    if not path.exists('project/'+ DB_NAME):
        db.create_all(app=app)
