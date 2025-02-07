# String Regex 1

## Python Regex

In this exercise, we will focus on the use and manipulation of text  in Python, including:

- Using the Python regex
- Creating custom regex patterns

## Tasks

### Task 1

Create a variable called `text` to store the data: `Berlin is a world city of culture, politics, media and science.` . Then search for the first white space character in the string and print its location using the appropriate label. 

- Your result should look like this:

```
The first white-space character is located at position: 6
```

### Task 2

Create a variable called `text` to store the data: `Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital.` . Then search for the word `Frankfurt` in the string . 

- Your result should look like this:

```
None
```

### Task 3

Create a variable called `text` to store the data: `Berlin is a city of culture.` . Replace the spaces with a hyphen.

- Your result should look like this:

```
Berlin-is-a-city-of-culture.
```

### Task 4

Create a variable called `text` to store the data: `Berlin is a city of culture.` . Search if the phrase `in` appears inside the string. Print the output of the regex function.

- Your result should look like this:

```
<re.Match object; span=(4, 6), match='in'>
```

### Task 5

Use the `text` variable from the previous task. Create a regular expression to look for any word that starts with an upper case "B". Print the position (start- and end-position) of the first match occurrence. 

- Your result should look like this:

```
(0, 6)
```

### Task 6

Create a variable called `text` to store the data: `The rain in Spain.`. Count how many times the subphrase `ai` appears in the string. Print the results on the screen.

- Your result should look like this:

```
2
```
