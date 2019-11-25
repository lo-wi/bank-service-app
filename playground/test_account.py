import unittest
from account import display_balance
from account import withdraw_money
from account import transfer

class TestDisplayBalance(unittest.TestCase):
    def test_first_user_correct_pin(self):
        displayed_amount = display_balance(1234, "user1")
        self.assertEqual(displayed_amount, "This is your current amount of money: 2000")
    #homework, positive tests
    def test_second_user_correct_pin(self):
        displayed_amount = display_balance(2222, "user2")
        self.assertEqual(displayed_amount, "This is your current amount of money: 3000")
    
    def test_third_user_correct_pin(self):
        displayed_amount = display_balance(3456, "user3")
        self.assertEqual(displayed_amount, "This is your current amount of money: 4000")

    def test_first_user_incorrect_pin(self):
        incorrect_pin = 1111
        correct_user = "user1"
        displayed_amount = display_balance(incorrect_pin, correct_user)
        self.assertEqual(displayed_amount, "INCORRECT PIN")
    
    #homework, edge cases
    def test_second_user_incorrect_pin(self):
        incorrect_pin = 1111
        correct_user = "user2"
        displayed_amount = display_balance(incorrect_pin, correct_user)
        self.assertEqual(displayed_amount, "INCORRECT PIN")

    def test_third_user_incorrect_pin(self):
        incorrect_pin = 1111
        correct_user = "user3"
        displayed_amount = display_balance(incorrect_pin, correct_user)
        self.assertEqual(displayed_amount, "INCORRECT PIN")

class TestWithdrawMoney(unittest.TestCase):
    #homework, positive cases
    def test_first_user_correct_pin_correct_amount(self):
        display_after_withdrawal = withdraw_money(1234, "user1", 500)
        self.assertEqual(display_after_withdrawal, "You have just withdrawn 500. Your new balance is 1500.")

    #homework, edge cases: incorrect pin
    def test_first_user_incorrect_pin_correct_amount(self):
        incorrect_pin = 1111
        correct_user = "user1"
        display_after_withdrawal = withdraw_money(incorrect_pin, correct_user, 500)
        self.assertEqual(display_after_withdrawal, "INCORRECT PIN")

    #homework, edge cases: ammount too big
    def test_first_user_correct_pin_incorrect_amount(self):
        display_after_withdrawal = withdraw_money(1234, "user1", 2500)
        self.assertEqual(display_after_withdrawal, "You are not allowed to withdraw more money than you have on your account.")

#homework, transfer_money, first_test
class TestTransferMoney(unittest.TestCase):
    def test_transfer_money_correct_user_correct_pin(self):
        pin=1234
        sender = "user1"
        receiver = "user2"
        money_to_transfer = 300
        result = "The amount 300 Euro were transferred to user2. Your current balance is 1700 Euro."
        updated_account = transfer(pin, sender, receiver, money_to_transfer) 
        self.assertEqual(updated_account, result)
    
    def test_transfer_money_second_correct_user_correct_pin(self):
        pin=2222
        sender = "user2"
        receiver = "user3"
        ##finish the tests and the function
        money_to_transfer = 300
        result = "The amount 300 Euro were transferred to user3. Your current balance is 2700 Euro."
        updated_account = transfer(pin, sender, receiver, money_to_transfer) 
        self.assertEqual(updated_account, result)

if __name__ == "__main__":
    unittest.main()