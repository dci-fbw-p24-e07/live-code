""" 
Task 2:
Keep the previous code and define now a global 
variable named default_settings as a dictionary with a 
key title, then create a function named get_title that 
takes one argument as a dictionary that defaults to 
default_settings and returns the content of the key 
title in the given dictionary.
"""

settings = {"title": "My very first title"}
default_settings = {"title": "These are the defaults"}


def change_site_title(new_title: str):
    """Changes the title of a site in a dictionary

    Args:
        new_title (_str_): The new title for the site
    """
    settings["title"] = new_title
    

def get_title(configurations=default_settings):
    """Gets the title of the site from dictionary"""
    return configurations['title']

print(get_title(settings))
print(get_title())
change_site_title("A new fancy title")
print(get_title(settings))
print(get_title())
