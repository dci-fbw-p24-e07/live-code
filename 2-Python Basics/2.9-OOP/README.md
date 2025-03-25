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

## 19.03.25 - OOP Principles and methods overriding in inheritance

- The pillars of OOP:
    1. Inheritance
    2. Encapsulation
    3. Polymorphism
    4. Abstraction
- Method overriding with inheritance
- How to override methods
- Tips on successful usage of OOP

### The pillars/principles of OOP

1. **Inheritance**

    - A way of creating a new class using details(code) from an existing class without modifying it.
    - The existing class is known as the parent(base) class
    - The newly class is known as the child(derived) class.
    - The child class can always be extended to have extra methods or attributes that may not be available in the parent class.
    - Any changes made on the parent will be effected on the child class. While changes made on the child class will just count as an extension on the child class.
    - Inheritance allows us to create objects that share code or logic yet are different.

    - In Python, we inherit by placing the name of the parent in parentheses after the name of the child class.

        ```python
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
                
        # Create object from animal class
        animal1 = Animal("Frost")       
        animal1.eat()

        # Create an object from the dog class
        dog1 = Dog("Jack")
        dog1.sleep()
        dog1.bark()
        ```

    **Multiple Inheritance:**

    - A class can be derived from more than one class.
    - This is achieved by placing the names of the parent classes in parentheses separated by commas(`,`) after the name of the child class.
    - The order in which the classes are inherited is very important.
    - If the parent classes have a method with the same name a technique known as MRO (Method Resolution Order) is used to determine which method should be inherited.
    - MRO specifies that the leftmost parent class' method will be inherited.

        ```python
        # Parent/Base class
        class Animal:
            
            def __init__(self, name):
                self.name = name
                
            def eat(self):
                print("I am eating.")
                
            def sleep(self):
                print("I am sleeping")

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
        ```

    **Multi-level Inheritance**

    - This is achieved when you create a child class from another child class.

        ```python
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
        ```



2. **Encapsulation**

    - Refers to the bundling of attributes and methods inside a single class.
    - It prevents outer classes from accessing and changing attributes and methods.
    - Also known as data hiding
    - Encapsulation seeks to hide the implementation details of objects from the outside. 
    - Itb states that all the important information is contained within the object - only selected data is available externally.
    - The inner workings are stored privately within the specified class
    - This provides security and control over object state changes, reduces risks of errors and makes the program more understandable.
    - In Python we denote private attributes/methods using underscore(`_`) as the prefix: i.e single `_` or double `__`

        ```python
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
        ```

3. **Polymorphism**

    - Simply means more than one form.
    - The same entity(method, operator or object) can perform different operations in different scenarios.
    - It complements inheritance by allowing different classes to perform actions with the same name but using different code.
    - In order for Polymorphism to be achieved inheritance needs to be implemented.
    - This is sometimes also known a s method overriding

        ```python
        class Vehicle:
    
            def refuel(self, litres):
                print(f"Refuelling with {litres} litres of fuel")
                

        class Truck(Vehicle):
            
            def refuel(self, litres):
                print(f"Refuelling with {litres} of Diesel.")

            
        class Bicycle(Vehicle):
            
            def refuel(self):
                print("I do not need fuel")


        vehicle_1 = Vehicle()
        vehicle_1.refuel(30)

        volvo_truck = Truck()
        volvo_truck.refuel(40)
        ```

4. **Abstraction**

    - Abstraction can be thought of as an expansion of encapsulation.
    - Each object only reveals a specific mechanism for usage.
    - It hides complex implementation details while just showing users the most crucial data and functions
    - In Python we can achieve abstraction by using abstract base classes which can be created using the `abc` (abstract base class) module and the `@abstractmethod` of the `abc` module.

### Tips for successful usage of OOP

1. Aim for simplicity and efficiency when designing OOP code.
2. Adhere to SOLID principles to prevent problems and keep code flexible, maintainable and easy to modify.
3. Identify the classes needed and their relationships to ensure programs function efficiently.
4. Employ abstraction to simplify understanding
5. Abide by programming standards and conventions to ensure code quality and maintainability.

## 20.03.25 - Types of methods, creating/using getters & setters

- Encapsulation in Python
- Different types of OOP methods:
    1. Instance method
    2. Class methods
    3. Static methods
- Public vs. Protected vs. Private attributes
- Creating and using getters & setter

### Encapsulation in Python

- In other OOP languages such Java or C++ encapsulation is strictly enforced with access modifiers such as `public`, `private` or `protected`

| Feature | Python | Java | C++ |
|---------|--------|------|-----|
| Access modifiers | No enforced modifiers; uses naming conventions: `_protected` or `__private` | Enforced access modifiers with `public`, `private` or `protected` keywords | Enforced access modifiers with `public`, `private` or `protected` keywords |
| Getter/setter methods | Optional, often used with `@property` decorator for controlled access | Common practice, typically implemented as methods | Common practice, typically implemented as methods |
| Data Access | Accessible via naming conventions; relies on developer discipline | Controlled by access modifiers; enforced by compiler | Controlled by access modifiers; enforced by compiler |
| Philosophy | "We are all adults here" - relies on conventions and trust | Strict enforcement of access control | Strict enforcement of access control | 

### Types of methods

- These are functions attached to a class or object.
- These define the actions that an object can perform
- They come in 3 basic categories:

1. **Instance methods**

    - The most common type of method.
    - They operate on a specific instance(object) of a class and have access to instance attributes using the `self` parameter

        ```python
        class Employee:
    
            def __init__(self, name):
                self.name = name

            # Instance method
            def greet(self):
                print(f"Hi, my name is {self.name} and I am new.")

            
        lisa = Employee("Lisa")
        lisa.greet() # Output: Hi, my name is Lisa and I am new.
        ```

2. **Class methods**

    - These are methods that are bound to the class itself.
    - They can access and modify class-level attributes using the `cls` parameter.
    - They are defined using the `@classmethod` decorator.

        ```python
        class Employee:
    
            hybrid = True
            
            def __init__(self, name):
                self.name = name

            # Class method
            @classmethod
            def get_hybrid(cls):
                return cls.hybrid
            
            @classmethod
            def set_hybrid(cls):
                cls.hybrid = False

            
        lisa = Employee("Lisa")
        lisa.set_hybrid()
        print(lisa.get_hybrid())
        ```

3. **Static methods**

    - These are not bound to either instance or class.
    - They essentially there for organizational purposes within the class
    - They do not have have access to either `self` or `cls` so they cannot modify attributes.
    - They defined using the `@staticmethod` decorator.

        ```python
        class Employee:
            
            hybrid = True
            
            def __init__(self, name):
                self.name = name
                
            # Static method
            @staticmethod
            def generate_passcode():
                return randint(1000, 9999999)

            
        lisa = Employee("Lisa")
        print(lisa.generate_passcode())
        ```

### Public vs Protected vs. Private attributes - Access modifiers

| Convention | Description | Example |
|------------|-------------|---------|
|  Public | Default access level; attributes and methods are accessible from outside the class | `self.attribute` |
| Protected | Indicated by a single underscore; a convention to denote partially restricted access. | `self._attribute` |
| Private | Indicated by double underscores; name mangling provides limited access restriction | `self.__attribute` | 

### Creating/Using getters and setters

- Getters and setters are methods created to give access to protected or private attributes without directly accessing them

**Using the `@property` decorator:**

```python
class Rectangle:
    
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        
    @property
    def height(self):
        return self.__height
        
rectangle_1 = Rectangle(10, 6)
print(rectangle_1.height)
rectangle_1.height = 8 # Output: AttributeError: can't set attribute 'height'
print(rectangle_1.height)
```

- Using the `@property` only produces a getter by default.
- It then allows you to access the private attribute as if it were a normal public attribute
- Trying to set a value without creating a setter will result in an `AttributeError`

**Creating a setter:**

```python
class Rectangle:
    
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        
    @property
    def height(self):
        return self.__height
    
    # Creating a setter
    @height.setter
    def height(self, new_height):
        self.__height = new_height
    
    @property
    def width(self):
        return self.__width
        
rectangle_1 = Rectangle(10, 6)
print(rectangle_1.height) # Output: 6
rectangle_1.height += 8
print(rectangle_1.height) # Output: 14
```

- To create a setter we would put a decorator with the name `@<getter-name>.setter` on the setter method (The getter being the method decorated with `@property`)
- This would allow modifying the attribute using normal assignment operations

**Defining getters**

```python
class Rectangle:
    
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    
    @property
    def width(self):
        return self.__width
    
    @width.getter
    def width(self):
        return f"The width is {self.__width}"
        
rectangle_1 = Rectangle(10, 6)
print(rectangle_1.width) # Output: The width is 10
```

- When a getter is explicitly defined it overrides the result of previous method defined with the `@property` decorator
- It is only useful in scenarios where you want to create some specific behaviour on the getter.

## 21.03.25 - Abstract Base Classes and Mixins

- What is an Abstract Class?
- Why use abstract classes in Python?
- Defining an Abstract Base Class
- The `abc` module
- What are Mixins?
- Implementing Mixins

### What is an Abstract Class?

- Is like a template for other classes
- It defines methods that must be included in any class that inherits from it, but it doesn't provide the actual code for those methods.
- some describe it as a recipe without specific ingredients - it tells you what steps follow but the details depend on the subclass.

**Why use abstract classes in Python?**

1. **Enforce method implementation:** An abstract class's methods function as a contract, requiring each subclass to implement its own version. This lowers the possibility of inconsistent or lacking implementations by ensuring specific functionality is present across all derived classes.
2. **Encourages code reuse:** abstract classes can have both concrete methods(implement actual functionality) and abstract methods(templates). The concrete greatly reduce code duplication and encourage the DRY(Do not Repeat Yourself) principle by providing shared functionality that can be inherited by all subclasses.
3. **Improve readability and maintainability:** Abstract classes help developers comprehend the structure and functionality of the software by providing a consistent and transparent framework. This structure makes the code easier to maintain by enforcing design principles like single responsibility and separation of responsibilities.
4. **Encourages polymorphism:** Abstract classes make it possible to write general code that works well with a variety of subclasses. Developers can create functions or methods that can handle any subclass of the abstract class thanks to the flexibility. This also increases code extensibility and adaptability to changes in future.

### Creating Abstract Classes in Python and the `abc` module

- The `abc` module in Python is used to implement abstract classes.
- This module offers tools to create these classes: `@abstractmethod` decorator and `ABC` class
- By using the decorator it ensures that each method must be implemented in the subclass
- In order to create a Abstract Base Class in Python you must inherit the `ABC` class provided by the `abc` module

    ```python
    # Import the abc module
    from abc import ABC, abstractmethod


    # Create an abstract class
    class Shape(ABC):  # inherit ABC class
        
        @abstractmethod
        def area(self):
            pass
        
        @abstractmethod
        def perimeter(self):
            pass
        
        # Concrete method
        def shape_name(self):
            print("I am a shape")
            

    class Circle(Shape):
        
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return 3.142 * self.radius ** 2
        
        def perimeter(self):
            return 2 * 3.142 * self.radius
        
            
    circle_1 = Circle(10.7)
    circle_1.shape_name()  # Output: I am a shape
    print(circle_1.perimeter()) # Output: 67.2388
    ```

    - Instantiating an object from a derived class that does not implement the abstract methods will raise an error

    ```python
    class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    # Missing area and perimeter implementation
    
    
    # This will raise an error      
    rectangle_1  = Rectangle(10.4, 5.7)  # Output: TypeError: Can't instantiate abstract class Rectangle with abstract methods area, perimeter
    ```

#### Challenge:

- Create an abstract called `Vehicle` that has 2 abstract methods of your choice and one concrete method of your choice. Add 2 attributes `model` and `mileage`
- Create 2 concrete subclasses from the abstract class
- Instantiate 1 object from each subclass

### Mixins

- A mixin is a class that provides method implementation for reuse by multiple related child classes. 
- A mixin is not intended for direct instantiation
- It bundles together a set of methods meant for reuse. Each mixin should have a single specific goal implementing closely related methods
- Typically a child class will use multiple inheritance to combine mixin classes
- Since Python does not outline a specific/formal way to define mixin classes it is good practice to name the mixin classes with the suffix `Mixin`
- The same rules for multiple will still apply especially with Method Resolution Order

    ```python
    class TelephoneMixin:
    
    # Concrete methods
    def dial_number(self, number):
        return f"Calling: {number}"
    
    
    class SMSMixin:
        
        def send_message(self, number, message):
            return f"To: {number}. \n Message: {message}"


    class VoIPPhone(TelephoneMixin, SMSMixin):
        
        def __init__(self, phone_number):
            self.phone_number = phone_number
            self.airtime = 0
            
        def topup(self, amount):
            self.airtime += amount


    phone_1 = VoIPPhone("+2579875323553")
    print(phone_1.send_message("+679999876755", "Hey there buddy!"))
    ```

## 25.03.25 - Dunder/Magic methods

- What are dunder methods?
- Implementing dunder methods
- Common examples:
    1. `__init__()`
    2. `__add__()`
    3. `__len__()`
    4. `__str__()`

### What are Dunder/Magic methods?

- These are special predefined methods that have two underscore prefixes and two underscore suffixes: `__method__`
- The methods are used in the case of operator overloading(They provide extended meaning beyond the predefined meaning of the operator)
- dunder methods can be better understood by visualizing a contract between your implementation and the Python interpreter. a contract usually has certain actions performed behind the scenes under given circumstances.
- The methods are invoked internally from the class based on a certain condition or action.
- Some dunder methods do not have a default implementation so they may raise errors when you try certain operations on those classes.


1. `__init__()`

    ```python
    class Car:
    
        # Instantiate an object
        def __init__(self, model):
            self.model = model

    
    car_1 = Car("Ford Mondeo")
    print(car_1)
    ```

2. `__str__()`

    - Used when representing an object as a string
    - Always returns a string
    

        ```python
        class Car:
    
            # Instantiate an object
            def __init__(self, model, mileage):
                self.model = model
                self.mileage = mileage
            
            # Define the string representation of an object
            def __str__(self):
                return str(f"{self.model} with {self.mileage} on the clock")

        
        car_1 = Car("Ford Mondeo", 2000)
        print(car_1)  # Output: Ford Mondeo with 2000 on the clock
        car_2 = Car("Volvo V40", 7000)
        print(car_2)  # Output: Volvo V40 with 7000 on the clock
        ```

3. `__add__()`

    - Performs the addition of specified attributes of the objects. 

    ```python
    class Distance:
    
        def __init__(self, x=None, y=None):
            self.feet = x
            self.inches = y
        
        def __add__(self, x):  # (dist_1, dist_2)
            # Create temporary distance
            # Placeholder object to store the results
            temp = Distance()
            # Add the feet attributes from both objects
            temp.feet = self.feet + x.feet
            # Add the inches attributes from both objects
            temp.inches = self.inches + x.inches
            if temp.inches >= 12:
                temp.feet += 1
                temp.inches -= 12
            return temp
        
        
    dist_1 = Distance(10, 4)
    dist_2 = Distance(16, 6)
    dist_3 = dist_1 + dist_2
    print(dist_3.feet)
    ```

4. `__len__()`

    - Is called when `len()` is invoked on ana object

        ```python
        class Car:
            
            # Instantiate an object
            def __init__(self, model, mileage):
                self.model = model
                self.mileage = mileage

            def __len__(self):
                letter_cnt = 0
                for letter in self.model:
                    letter_cnt += 1
                return letter_cnt
                    
        
        car_1 = Car("Ford Mondeo", 2000)
        print(len(car_1))



