""" 
Task 3: Default and non default arguments combined
"""

settings = {"title": "My very first title"}
default_settings = {"title": "These are the defaults"}

settings["pages"] = []
default_settings["pages"] = []


def get_pages(settings=default_settings):
    """Return the list stored in the key pages of the given settings dictionary.

    Args:
        settings (_type_, optional): _description_. Defaults to default_settings.
    """
    return settings["pages"]

def add_page(page: dict, settings=default_settings):
    """Adds the given page to the settings dictionary

    Args:
        page (dict): Contains the page details
        settings (_type_, optional): _description_. Defaults to default_settings.
    """
    settings["pages"].append(page)
    

home = {"title": "Home", "path": "/"}
add_page(home)
print(get_pages())
print(get_pages(settings))
about = {"title": "About", "path": "/about/"}
add_page(about, settings)
print(get_pages())
print(get_pages(settings))
