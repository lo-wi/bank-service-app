user_data = {"user1": [1234, 2000], "user2": [2222, 3000], "user3": [3456, 4000]}

def display_balance(pin, user):
    if pin == user_data[user][0]:
        return "This is your current amount of money: {amount}".format(amount = user_data[user][1])
    else:
        return "INCORRECT PIN"

def withdraw_money(pin, user, amount):
        if pin == user_data[user][0]:
            if amount <= user_data[user][1]:
                user_data[user][1] = user_data[user][1] - amount
                return "You have just withdrawn {}. Your new balance is {}.".format(amount, user_data[user][1])
            else: return "You are not allowed to withdraw more money than you have on your account."
        else:
            return "INCORRECT PIN"

def transfer(pin, sender, receiver, money):
    balance = user_data[sender][1]
    balance -= money
    return "The amount 300 Euro were transferred to {}. Your current balance is {} Euro.".format(receiver, balance)
    ##finish the function