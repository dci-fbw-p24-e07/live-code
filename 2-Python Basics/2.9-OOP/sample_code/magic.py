"""  
Dunder/Magic methods and their usage
"""

class Car:
    
    # Instantiate an object
    def __init__(self, model, mileage):
        self.model = model
        self.mileage = mileage
    
    # Define the string representation of an object
    def __str__(self):
        return str(f"{self.model} with {self.mileage} on the clock")

    def __len__(self):
        letter_cnt = 0
        for letter in self.model:
            letter_cnt += 1
        return letter_cnt
            
 
car_1 = Car("Ford Mondeo", 2000)
print(len(car_1))
car_2 = Car("Volvo V40", 7000)
print(car_2)


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
    