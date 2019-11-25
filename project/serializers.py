class UserSerializer:
    @staticmethod
    def serialize(user):
        return {"id": user.id,
                "name": user.name,
                "pin": user.pin,
                "balance": user.balance}