"""Convert file to binary."""


with open("../data/task1.txt") as source:
    content = source.read()
    with open("../data/task1.bin", "wb") as target:
        target.write(content.encode("utf-8"))

# Or

with open("../data/task1.txt") as source, \
     open("../data/task1.bin", "wb") as target:

    target.write(source.read().encode("utf-8"))
