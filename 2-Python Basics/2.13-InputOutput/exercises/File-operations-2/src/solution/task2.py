"""Creating text files without overwriting."""


files = [
    {
        "name": "todos.txt",
        "content": ["My ToDos:", "", "Go shopping", "Finish module"]
    },
    {
        "name": "bookmarks.txt",
        "content": ["My links:", "", "https://google.com", "https://digitalcareerinstitute.org"]
    }
]

for file in files:
    with open(file["name"], "x") as target:
        # Add a line break to each line
        lines = [f"{line}\n" for line in file["content"]]
        target.writelines(lines)
