# File: mysite/__init__.py

from flask import Flask
app = Flask(__name__)
app.config.from_object('config')

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

from mysite import models
from mysite import views
