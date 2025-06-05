"""Appending text to a file."""


additions = [
    {
        "name": "todos.txt",
        "content": ["Call mom", "Walk the dog"]
    },
    {
        "name": "bookmarks.txt",
        "content": ["https://python.org", "https://www.djangoproject.com/"]
    }
]

for file in additions:
    with open(file["name"], "a") as target:
        # Add a line break to each line
        lines = [f"{line}\n" for line in file["content"]]
        target.writelines(lines)
