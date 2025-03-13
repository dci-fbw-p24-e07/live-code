"""
Object Oriented Programming Basics
"""


# Define a class called Car
class Car:
    """
    A car class for our example
    """
    
    # Class attributes
    num_of_wheels = 4
    spare_tyres = 1

    def __init__(self, colour, model, fuel_type, mileage: int):
        # Instance attributes
        self.colour = colour
        self.model = model
        self.fuel_type = fuel_type
        self.mileage = mileage
        self.num_of_owners = 1
        
    # Defining methods
    def forward(self):
        print(f"We are moving forward in the {self.model}")
        
    def reverse(self):
        print("We are moving backwards")
        
    def refuel(self, num_of_litres: int):
        print(f"Please give me {num_of_litres} litres of {self.fuel_type}")
  

# Instantiate a Mazda
mazda = Car("Green", "Demio", "Petrol", 15000)
print(mazda.colour)

# Changing an attribute value
mazda.colour = "Purple"

# Accessing the attributes
print(mazda.colour)
print(mazda.model)
print(mazda.num_of_wheels)

# Changing the class attribute
Car.num_of_wheels = 6

# Instantiate an Audi
audi = Car(colour="Red", model="A4", fuel_type="Petrol", mileage=75000)
print(audi.num_of_wheels)

# Using methods
audi.forward()
mazda.forward()
mazda.reverse()

audi.refuel(35)
