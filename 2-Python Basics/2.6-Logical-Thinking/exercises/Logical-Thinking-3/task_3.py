""" 
Task 3
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
        

def author_is_popular(author_name: str) -> bool:
    author = get_author(author_name)
        
    return bool(author and author["items"] and (sum([
        article["reads"] for article in author["items"]
        if "reads" in article and article["status"] == "Published"
    ]) / len(author["items"])) > 1000)


print("Clark", author_is_popular("Clark"))
print("Peter", author_is_popular("Peter"))
print("Samantha", author_is_popular("Samantha"))
print("Mathilda", author_is_popular("Mathilda"))
print("Mario", author_is_popular("Mario"))
    
