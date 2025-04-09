from animal import Animal

class Dog(Animal):

    def __init__(self):
        super().__init__(4, 2) # Initializing animal with 4 legs and 2 eyes

    def breathe(self):
        super().breathe()
        print("Dogs love to breathe with their mouths open.")

    def walk(self):
        super().walk()
        print("Dogs love to run.")
