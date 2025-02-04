from collections import namedtuple

reg_tuple = ("Sammy", "Jones", 1233443)
print(reg_tuple)

# Create a class to represent students
Student = namedtuple("Student", ["fname", "lname", "sid"])

# Create a student object using the Student class
mary = Student("Mary", "Fisher", 1245678)

# access first name
print(mary[0])
print(mary.fname)
