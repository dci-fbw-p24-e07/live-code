from collections import deque

students = ["Sammy", "Mary", "Jordan"]

# insert to beginning of list
students.insert(0, "Alice")

# initialize a list using the deque class
students_dq = deque(["Sammy", "Mary", "Jordan"])

# Insert to the beginning of list
students_dq.appendleft("Alice")

greet = "hello", "world"

print(students)
print(students_dq)
print(greet)
