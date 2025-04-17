class InsufficientAmount(Exception):
    pass


class Wallet:
    
    def __init__(self, initial_amount=0):
        self.balance = initial_amount
        
    def pay(self, amount):
        if self.balance < amount:
            raise InsufficientAmount("Not enough funds to pay for that.")
        self.balance -= amount
        return self.balance
        
    def get_cash(self, amount):
        self.balance += amount
        return self.balance
