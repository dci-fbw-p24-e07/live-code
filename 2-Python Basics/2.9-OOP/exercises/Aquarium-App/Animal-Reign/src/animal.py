class Animal:

    def __init__(self, number_of_legs: int, number_of_eyes: int):
        self.number_of_legs = number_of_legs
        self.number_of_eyes = number_of_eyes

    def get_number_of_legs(self):
        return self.number_of_legs

    def get_number_of_eyes(self):
        return self.number_of_eyes

    def breathe(self):
        print("The " + type(self).__name__ + " is breathing.")

    def walk(self):
        print("Walking with [" + str(self.get_number_of_legs()) + "] legs.")

    def summary(self):
        print(
            "This is an instance of [" + type(self).__name__ + "]. It has ["
            + str(self.get_number_of_legs())
            + "] legs and ["
            + str(self.get_number_of_eyes()) + "] eyes."
        )
