"""
Task 2
"""

users = [
    {
        "name": "Clark",
        "type": "Publisher",
        "items": [
            {
                "title": "The ABC of Blockchain",
                "status": "Draft",
                "reads": 10
            }
        ]
    },
    {
        "name": "Peter",
        "type": "Publisher",
        "items": []
    },
    {
        "name": "Samantha",
        "type": "Publisher",
        "items": [
            {
                "title": "The ABC of JavaScript",
                "status": "Published",
                "reads": 3254
            },
            {
                "title": "The XYZ of JavaScript",
                "status": "Published",
                "reads": 226
            }
        ]
    },
    {
        "name": "Mathilda",
        "type": "Reviewer",
        "items": [
            {
                "title": "The ABC of Blockchain",
                "status": "Pending"
            }
        ]
    }
]


def get_author(author_name):
    """Return the author dictionary"""
    for user in users:
        if user["name"] == author_name:
            return user
        
        
def author_average_reads(author_name: str) -> int:
    author = get_author(author_name)
    reads_average = 0
    if author and author["items"]:
        total_reads = 0
        for article in author["items"]:
            if article["status"] == "Published":
                total_reads += article["reads"]
                
        reads_average = total_reads / len(author["items"])
    
    return int(reads_average)


print("Clark", author_average_reads("Clark"))
print("Peter", author_average_reads("Peter"))
print("Samantha", author_average_reads("Samantha"))
print("Mathilda", author_average_reads("Mathilda"))
print("Mario", author_average_reads("Mario"))
