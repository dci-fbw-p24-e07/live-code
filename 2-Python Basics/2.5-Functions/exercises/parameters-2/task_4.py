""" 
Task 4
"""

def print_user_profile(gender="female", first=None, last="Doe", pictures=[]):
    if not (len(pictures) == 1 and pictures[0] == "common_header.png"):
        pictures.insert(0, "common_header.png")
    if first is None:
        if gender == "female":
            first = "Jane"
        else:
            first = "John"
    print(f"The user {first} {last} has the following pictures")
    for picture in pictures:
        print(picture)


test_data1 = {
    "gender": "male",
    "last": "Brown",
    "pictures": ["holidays1.png", "easter_grandma.png"]
}
test_data2 = {
    "first": "Alicia",
    "last": "Schmidt"
}
test_data3 = {
    "last": "Korkov",
    "pictures": ["sunset.png"]
}
print_user_profile(**test_data1)
print_user_profile(**test_data2)
print_user_profile(**test_data3)
print_user_profile(**test_data2)
