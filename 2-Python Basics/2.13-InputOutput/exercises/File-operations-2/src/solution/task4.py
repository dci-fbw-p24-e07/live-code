"""Changing fragments of a text file."""


changes = [
    {
        "name": "todos.txt",
        "change": ("Call mom", "Clean up house")
    },
    {
        "name": "bookmarks.txt",
        "change": ("https://google.com", "https://www.w3resource.com")
    }
]

for file in changes:
    text_from = file["change"][0]
    text_to = file["change"][1]
    with open(file["name"], "r+") as target:
        content = target.read()
        start = content.index(text_from)
        end = start + len(text_from)
        suffix = content[end:]
        target.seek(start)
        target.write(text_to + suffix)
