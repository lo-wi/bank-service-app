from flask import Flask, escape, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db=SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'


from project import controller

