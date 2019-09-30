from flask import jsonify
from project import app
from project.models import User

@app.route('/')
def hello():
    return "<h2>Hello World!</h2>"

@app.route('/about')
def about():
    return "<h2>About me</h2>"


@app.route('/users')
def getUsers():
    user=User.query.first()
    return jsonify(user.name)
