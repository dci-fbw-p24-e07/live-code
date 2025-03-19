""" 
Polymorphism sample code
"""


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
