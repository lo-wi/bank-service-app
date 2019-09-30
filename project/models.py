from project import db
#creating models
class User(db.Model):
    id=db.Column(db.Integer, primary_key=True) #setting id to primary key; meaning that it cannot be duplicated
    name=db.Column(db.String(50), unique=True) #String requires limit; otherwise the database memory could be killed by adding really long names
    pin=db.Column(db.Integer, nullable=False)
    balance=db.Column(db.Integer)

    def __repr__(self):
        return f"User(id='{self.id}', pin='{self.pin}', name='{self.name}', balance='{self.balance}' )"

