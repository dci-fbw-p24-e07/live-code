# Generate an invite for each friend in the list

for friend in ["Marvin", "Louisa", "Jack", "Sonic"]:
    invitation = "Hi " + friend + ". Please come to my party!"
    print(invitation)

# Get the employee name for each of the employees

employees = {
    "Manager": "Jack",
    "Developer": "Ross",
    "DB Engineer": "Mary",
    "Network Admin": "Louisa"
}

for emp in employees:
    print(employees[emp])

for emp in employees.values():
    print(emp)

# Generate a countdown timer

for i in range(100):  # Generates variables from 0 to 9
    print("I will always do my homework")
    
# print out the numbers 1 - 12 with their squares - 7^2
for x in range(1, 13):
    print(x, x**2)
    