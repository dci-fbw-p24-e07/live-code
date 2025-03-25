class Author:
    
    def __init__(self, name: str, email: str, gender: str):
        self._name = name
        self._email = email
        self._gender = gender
        
    def get_name(self) -> str:
        return self._name
    
    def get_email(self) -> str:
        return self._email
    
    def set_email(self, new_email: str):
        self._email = new_email
        
    def get_gender(self) -> str:
        return self._gender
    
    def __str__(self) -> str:
        return str(f"Author [name={self._name}, email={self._email}, gender={self._gender}]")
