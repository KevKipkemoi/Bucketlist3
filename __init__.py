from flask import Flask, request, render_template, flash, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import sha256_crypt
from flask_login import LoginManager
from app.forms import SignUpForm, LoginForm, EditForm
from app.forms import GoalsForm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_wtf.csrf import CsrfProtect

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
CsrfProtect(app)

engine = create_engine('sqlite:///goals.db', echo = True)
Session = sessionmaker(bind=engine)
session = Session()

lm = LoginManager()
lm.init_app(app)
lm.login_view = "login"

from app import views, models
