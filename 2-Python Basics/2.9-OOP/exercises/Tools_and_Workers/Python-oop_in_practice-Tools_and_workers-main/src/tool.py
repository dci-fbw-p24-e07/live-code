# Do not modify this class
class Tool:
    def work(self):
        raise NotImplementedError("Abstract Method not implemented")


# Write your code here to implement the Laptop class correctly
class Laptop(Tool):
    
    def work(self):
        print("Laptop is running")



