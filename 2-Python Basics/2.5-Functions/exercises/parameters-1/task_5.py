""" 
Positional and keyword arguments + default values
"""


def pig_latin(*texts, suffix="ay", single=False) -> list | str:
    """Translates the given text to pig latin 

    Args:
        suffix (str, optional): The suffix to add to each word. Defaults to "ay".
        single (bool, optional): Determines whether it should be a single string output. Defaults to False.

    Returns:
        list | str: output depending on whether single string or not.
    """
    vowels = "aeiou"
    pig_latin_version = []
    for text in texts:
        # separate each word in the text
        words = text.split(" ")
        # Loop over words list
        for word in words:
            # Check if word starts with a vowel
            first_letter = word[0].lower()
            if first_letter in vowels:
                # Add suffix to the end
                pig_latin_word = word + suffix
                # Add final word to list
                pig_latin_version.append(pig_latin_word.capitalize())
            
            else:
                # Move the first letter to the end and add suffix
                pig_latin_word = word[1:] + first_letter + suffix
                # Add final word to list
                pig_latin_version.append(pig_latin_word.capitalize())
                
    # if single concatenate into 1 string
    if single:
        # return concatenated text
        return " ".join(pig_latin_version)
    # return pig latin list
    return pig_latin_version


test1_data = ["Word", "Apple"]
test1_config = {}

test2_data = ["Python", "Functions"]
test2_config = {"suffix": "oy"}

test3_data = ["If the word starts with a vowel", "add the suffix to the word"]
test3_config = {"single": True, "suffix": "ep"}


print(pig_latin(*test1_data, **test1_config))
print(pig_latin(*test2_data, **test2_config))
print(pig_latin(*test3_data, **test3_config))
