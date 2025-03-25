from author import Author

class Book:
    
    def __init__(self, name: str, author: Author, price: float, qty: int = 0):
        self._name = name
        self._author = author
        self._price = price
        self._qty = qty
    
    def get_name(self) -> str:
        return self._name
    
    def get_author(self) -> Author:
        return self._author
    
    def get_price(self) -> float:
        return self._price
    
    def set_price(self, new_price: float):
        self._price = new_price
        
    def get_qty(self) -> int:
        return self._qty
    
    def set_qty(self, new_qty: int):
        self._qty = new_qty
    
    def __str__(self):
        return str(
            f"Book[name={self._name}, {self._author}, price={self._price}, qty={self._qty}]"
        )
    