# Using read mode(default)
with open("dummy.txt") as file_1:
    contents = file_1.read()
    print(contents)

# # Using write mode
file_2 = open("dummy.txt", "w")

file_2.write("We are going to have another 4 day weekend")

file_2.close()

# Opening a file in binary mode

with open("example.txt", "wb") as file_3:
    data = b"\x48\x65\x6C\x6C\x6F"
    file_3.write(data)
    
