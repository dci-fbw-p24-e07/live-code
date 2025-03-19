""" 
Encapsulation sample code
"""


class Product:
    
    def __init__(self):
        self.__max_price = 1000
        self._discount = 0.1
    
    def sell(self):
        if self._discount:
            price = self.__max_price - (self.__max_price * self._discount)
            print(f"We are selling for {price}")
            
        else:
            print(f"We are selling for {self.__max_price}")
    
    # Setter methods
    def set_max_price(self, new_price):
        self.__max_price = new_price
        
    def set_discount(self, new_discount):
        self._discount = new_discount
        
        
radio = Product()

radio.sell()
# Using the setter function
radio.set_max_price(2000)
radio.sell()
