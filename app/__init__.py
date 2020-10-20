# Import flask and template operators
from flask import Flask, render_template

# Import Peewee
from config import DATABASE
from peewee import SqliteDatabase

from flask_login import LoginManager

# Define the WSGI application object
letstalk = Flask(__name__)

# CSRF
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()
csrf.init_app(letstalk)


# Configurations
letstalk.config.from_object('config')


# Define the database object which is imported
# by modules and controllers
db = SqliteDatabase(DATABASE)

login_m = LoginManager()
login_m.init_app(letstalk)

from app.controllers import views

from app.models.tables import *
db.create_tables([User, Post])