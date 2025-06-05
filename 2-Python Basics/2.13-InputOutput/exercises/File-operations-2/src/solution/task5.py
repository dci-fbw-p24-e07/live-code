"""Reading, writing and manipulating content."""


with open("todos.txt", "r") as source, open("todos.secret", "w") as target:
    content = source.read()
    for char in content:
        code = str(ord(char))
        target.write(f"{code}\n")

with open("todos.secret", "r") as todos:
    readable = ""
    for num in todos:
        readable += chr(int(num))
    print(readable)
