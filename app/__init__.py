import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = "SUPERCALIFRAGILISTICSECRETKEY"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/mydatabase.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://capstone:password@localhost/capstoneproject'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://ubuntu:password-01@localhost/CAPSTONE'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
# app.debug = True

db = SQLAlchemy(app)
CSRF_ENABLED = True

# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'


UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'uploads')

ALLOWED_EXTENSIONS = {"png", 'jpg', 'jpeg', 'gif'}


app.config.from_object(__name__)
from app import views, models 
