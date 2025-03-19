""" 
Inheritance sample code
"""


# Parent/Base class
class Animal:
    
    def __init__(self, name):
        self.name = name
        
    def eat(self):
        print("I am eating.")
        
    def sleep(self):
        print("I am sleeping")
        

# Child/Derived class
class Dog(Animal):
        
    def bark(self):
        print("Woof woof!")
        
class Puppy(Dog):
    pass

puppy1 = Puppy("Sparkie")
puppy1.eat()
puppy1.sleep()
puppy1.bark()
        
# Create object from animal class
animal1 = Animal("Frost")       
animal1.eat()

# Create an object from the dog class
dog1 = Dog("Jack")
dog1.sleep()
dog1.bark()


class Mammal:
    
    def give_birth(self):
        print("My child is fully-formed")
        
    def eat(self):
        print("I am eating as a mammal")
    
    
class Cat(Mammal, Animal):
    pass


garfield = Cat("Garfield")
garfield.eat()
garfield.sleep()
garfield.give_birth()

