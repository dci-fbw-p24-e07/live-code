""" 
Task 1
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


# def has_hits(author_name: str) -> bool:
#     for user in users:
#         if user["name"] == author_name:
#             articles = user["items"]
#             if articles:
#                 for article in articles:
#                     if "reads" in article.keys():
#                         if article["reads"] > 1000:
#                             return True
#     return False

def get_author(author_name):
    """Return the author dictionary"""
    for user in users:
        if user["name"] == author_name:
            return user

      
def check_hits(author_info: dict):
    """Return True if author has article with more than 1000 reads."""
    for article in author_info["items"]:
        if "reads" in article.keys() and article["reads"] > 1000:
            return article
        
        
def has_hits(author_name: str) -> bool:
    """Return True if author exists AND has hits"""
    author = get_author(author_name)
    return bool(author and check_hits(author))


print("Clark", has_hits("Clark"))
print("Peter", has_hits("Peter"))
print("Samantha", has_hits("Samantha"))
print("Mathilda", has_hits("Mathilda"))
print("Mario", has_hits("Mario"))
