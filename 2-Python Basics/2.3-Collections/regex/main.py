import re

# `findall()`
string_1 = "hello 12 hi. 89 how a876e you? 56"
pattern_1 = "[0-9]+"  # Search for 1 or more occurrences of a digit

string_2 = "johnny76@mail.com"
pattern_2 = "^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+.[a-z.]$"

result = re.findall(pattern=pattern_1, string=string_1)
result_2 = re.findall(pattern=pattern_2, string=string_2)

# Find all valid emails in the given list
# list_1 = ["johnny76@mail.com", "mary@in", "@linked.com", "marcus@fancy.co.uk"]

# for string in list_1:
#     print(re.findall(pattern_2, string))

print(result)
print(result_2)

# `split()`

pattern_3 = "[0-9]+"

string_3 = "hello 12 hi. 89 how a876e you? 56"
string_4 = "Twelve:12 Eighty-nine:89 seventy-six:76"

result_3 = re.split(pattern=pattern_3, string=string_3)
result_4 = re.split(pattern=pattern_3, string=string_4)

print(result_3)
print(result_4)

# `sub()`
# Program to remove all whitespaces
string_5 = "abc 12\n def      15 \n 56 \nghi"

pattern_4 = "\s+"
replace = ""

result_5 = re.sub(pattern_4, replace, string_5, 1)

print(result_5)

# `search()`
# Check if a phone number starts with the country code
string_6 = "+26 5 899654937"
string_7 = "08754456323"

pattern_5 = "^[+][0-9]{1,3}"  # Alternatives: "^[+]{1}[0-9]{1,3}", "^(\+|(00))[0-9]{1,3}"

result_6 = re.search(pattern_5, string_6)
result_7 = re.search(pattern_5, string_7)

print(result_6)  # Output: <re.Match object; span=(0, 4), match='+265'>
print(result_7)  # Output: None


# `search().group()`
string_8 = "39801 356, 2102 1111"
pattern_6 = "([0-9]{3}) ([0-9]{2})"  # The brackets determine separate grouping for the pattern

result_8 = re.search(pattern_6, string_8).group(1, 2)

print(result_8)

# Raw string prefixing

string_9 = "\n and \r are escape + sequences()[]"
pattern_7 = r"[\n+()[]]"

result_9 = re.findall(pattern_7, string_9)
print(result_9)
