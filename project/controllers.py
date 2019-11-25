from flask import request #first you import things from outside
from flask import jsonify, request


from project import app #siehe init-file
from project import db
from project.models import User
from project.serializers import UserSerializer


@app.route('/')
def hello():
    return 

@app.route('/about')
def about():
    return "<h2>About me</h2>"


@app.route('/users', methods=["GET"])
def show_users():
    users=User.query.all()
    results=[]
    for user in users:
        serialized_user=UserSerializer.serialize(user)
        results.append(serialized_user)
    return jsonify(results)

@app.route('/users', methods=["POST"])
def create_user():
    body = request.get_json()
    name=body.get("name")
    pin=body.get("pin")
    balance=body.get("balance")
    
    new_user=User(name=name, pin=pin, balance=balance)
    db.session.add(new_user)
    db.session.commit()
    return "OK"

@app.route('/users/<name>', methods=["DELETE"])
def delete_user(name):
    User.query.filter_by(name=name).delete()
    db.session.commit()
    return "Deleted"

@app.route('/balance')
def display_balance():
    pin = int(request.args.get('pin'))
    user = request.args.get('name')
    user_data=User.query.filter_by(name=user).first()
    if pin == user_data.pin:
        return "Current amount of money: {}.".format(user_data.balance)
    else:
        return jsonify({"Error":"INCORRECT PIN"})

@app.route('/withdraw', methods=["PUT"])
def withdraw_money():
    body = request.get_json()
    name=body.get("name")
    pin=body.get("pin")
    amount_to_withdraw=body.get("amount to withdraw")
    user_data=User.query.filter_by(name=name).first()
    if pin == user_data.pin:
        if amount_to_withdraw <= user_data.balance:
            user_data.balance=user_data.balance-amount_to_withdraw
            db.session.add(user_data)
            db.session.commit()
            return jsonify(UserSerializer.serialize(user_data))    
        else:
            return "Insufficient funds"
    else:
        return "INCORRECT PIN"

#endpoint looking for a user, using id - get request - endpoint would be users/id - serializer needs to give us the id of the user

@app.route('/search_by_id', methods=['GET'])
def show_user_by_id():
    user = request.args.get('id')
    user_data=User.query.filter_by(id=user).first()
    return "The name of the user is: {}.".format(user_data.name)
    
