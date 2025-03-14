# Object Oriented Programming - OOP

## 13.03.25 - OOP Introduction

- What is OOP?
- How to create Classes?
- Class vs object/instance
- Instantiating objects - Creating objects - creating instances
- The `self` keyword
- Attributes/properties in a class
- Methods in a class
- Passing arguments to methods

### What is OOP?

- Is based on the programming paradigm that uses statements to change a programs state. Mainly focusing on how the program should operate
- OOP uses concepts of objects and classes. 
- A class can be thought of as a blueprint for creating objects.
- Objects can have their own attributes/properties(characteristics they possess) and methods ( actions they can perform)
- OOP allows a modular design pattern for programs, allowing us to separate different of objects and the functionalities while still allowing for reusability.

### Classes vs Objects/Instances

- A class can be used to create as many objects as possible
- An object is always going to be independent of other objects

![Classes vs. Objects](example_imgs/Classes_vs_Objects.png)

### Creating Classes

- To define a Python class we use the keyword `class` followed by the class name and a colon(`:`)
- The class name must always be capitalized
- Inside this class an `__init__` method is supposed to be defined. This is the initializer/constructor that will be used to instantiate objects.
- `__init__` must always be present, it takes 1 argument which the `self` keyword.

```python
# Define a class called Car
class Car:
    """
    A car class for our example
    """

    def __init__(self):
        pass
```

### Instantiating Objects/Creating Objects

- To instantiate an object, type the class name, followed by parentheses.
- You can assign this to a variable in order to keep track of it.

```python
# Instantiate a Mazda

mazda = Car()
print(mazda)

# Instantiate a Audi
audi = Car()
print(audi)
```

### Challenge 1

1. Create a class called Employee and instantiate 2 objects from this class

    ```python
    class Employee:

        def __init__(self):
            pass

    greg = Employee()
    janice = Employee()
    ```

2. Create a class called Animal and instantiate 2 objects from this class

    ```python
    class Animal:

        def __init__(self):
            pass

    parrot = Animal()
    elephant = Animal()
    ```

### The `self` keyword

- Is used to represent an instance(object) of a class.
- It becomes very important when referring to attributes and methods within the class
- It allows the separation of instances and their attributes and methods

### Defining Attributes

**Instance Attributes**

- Attributes/Properties are what defined the object(characteristics)
- These are usually defined in the `__init__` method.

```python
# Define a class called Car
class Car:
    """
    A car class for our example
    """

    def __init__(self, colour, model, fuel_type, mileage: int):
        # Instance attributes
        self.colour = colour
        self.model = model
        self.fuel_type = fuel_type
        self.mileage = mileage
        self.num_of_owners = 1
    

# Instantiate a Mazda
mazda = Car("Green", "Demio", "Petrol", 15000)
print(mazda)

# Instantiate an Audi
audi = Car(colour="Red", model="A4", fuel_type="Petrol", mileage=75000)
print(audi)
```

**Accessing attributes:**

- To access an attribute we use dot notattion.
- This is done by typing the name of the object, followed by a dot and the attribute's name
    
    ```python
    # Instantiate a Mazda
    mazda = Car("Green", "Demio", "Petrol", 15000)
    print(mazda)

    # Accessing the attributes
    print(mazda.colour)
    print(mazda.model)
    ```

**Class Attributes**

- These are universal attributes that cover all instantiated objects.
- They serve as a common attribute that can cut across all objects created from the class
- They sometimes serve as defaults
- Class attributes are defined outside of the `__init__` method and just after the class declaration
- There is no need to use the `self` keyword
- In order to change a class attribute you would need to access through the class itself and not an instantiated object.

```python
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

# Instantiate a Mazda
mazda = Car("Green", "Demio", "Petrol", 15000)
print(mazda.num_of_wheels) # Output: 4

# Changing the class attribute
Car.num_of_wheels = 6

# Instantiate an Audi
audi = Car(colour="Red", model="A4", fuel_type="Petrol", mileage=75000)
print(audi.num_of_wheels) # Output: 6
```

### Challenge 2 

1. Add 5 attributes of your choice to your Employee class and access at least 3 of them

    ```python
    class Employee:

        def __init__(self, first_name, last_name, age, employee_id, department):
            self.first_name = first_name
            self.last_name = last_name
            self.age = age
            self.employee_id = employee_id
            self.department = department
            

    greg = Employee("Greg", "Brown", 42, 13467, "Marketing")
    print(f"{greg.first_name} {greg.last_name} is part of the {greg.department} department.")
    ```

2. Add 5 attributes of your choice to your Animal class and access at least 3 of them elephant = Animal()

    ```python
    class Animal:

        def __init__(self, name, species, age, height, weight):
            self.name = name
            self.species = species
            self.age = age
            self.height = height
            self.weight = weight

    parrot = Animal(name="Peter", species="Grey parrot", age=3, height="10cm", weight="1.5kgs")

    print(f"{peter.name} the {peter.species} is {peter.age} years old.")
    ```

### Defining methods

- Methods are the functionalities of the class
- These help to change the state of objects or perform object tasks/actions
- They are basically functions defined under the class
- In order to define a method we use the `def` keyword, followed by the name of the method, followed by parentheses with the `self` keyword as the first parameter and then a colon (`:`)
- Any other methods will come after the initializer(or any dunder methods)


```python
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

# Using methods
audi.forward()
mazda.forward()
mazda.reverse()
```

### Passing arguments to methods

- When defining methods any parameters are supposed to be declared after the `self` keyword
- These parameters can still be declared and used just like regular function parameters

```python
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

# Using methods
audi.forward()
mazda.reverse()
audi.refuel(35)
```
