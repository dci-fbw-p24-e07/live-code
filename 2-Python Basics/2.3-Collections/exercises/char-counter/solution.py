def count_characters(word):
    counts = {}
    
    for char in word.lower():
        # add the key and set the default value to zero
        counts.setdefault(char, 0)
        counts[char] = counts[char] + 1
        
    return counts
    
    
print(count_characters("Elephant"))

# OR

from collections import Counter

def count_characters(word):
    result = Counter(word.lower())
    return result

print(count_characters("Elephant"))