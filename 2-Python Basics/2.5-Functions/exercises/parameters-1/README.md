# Function parameters

## Description

In this exercises, we will focus on simple functions and parameter definition and usage.

*In each function created throughout these exercises the body of the function must contain a **dosctring** (a first line with a string explaining what the function does).*

##

## Tasks

###

### Task 1: Simple functions with single positional arguments

Create two simple functions `isOdd` and `isEven` that each take a single Integer and return a Boolean indicating whether the passed value is odd or is even.

*An integer is even if it can be divided by 2 to produce another integer value. It is odd when dividing it by two produces a decimal value.*

Then use those functions with these test cases:

```
print(isOdd(1), isEven(1))
print(isOdd(657842), isEven(657842))
print(isOdd(0), isEven(0))
```

- Your result should look like this:

```
True False
False True
False True
```

###

### Task 2: Multiple positional arguments of different types

Create a single function `getParity` that does the same thing as the two functions in the previous task. This new function will accept a new positional argument of type String that will contain the type of parity we want to get (either `odd` or `even`).

If the argument parity is different than `odd` and `even` then it should output a string message `Parity indicated is unknown`.

Then design your own test cases to replicate the ones in the previous task but using the new function. Add also the following test case at the end:

```
print(getParity(-2, 'number'))
```

- Your result should look like this:

```
True False
False True
False True
Parity indicated is unknown
```

###

### Task 3: Multiple keyword arguments of different types

Create a single function `greet` that greets a person differently depending on the time of the day.

To do that, you will need to define two parameters on the header, one of type `String` and the other one of type `Date`. You must define them as **keyword arguments** and name them `name` and `date`.

If the time of the date is before 12:00PM the function will return "Good Morning, *name_of_the_person*!", if not it will return "Good Afternoon, *name_of_the_person*!".

*You can extended it to say Good Night at another time, if you like*.

Use the following test cases:

```
print(greet(
    name="John",
    date=datetime.datetime(2021, 5, 7, 11, 59, 59)
    ))
print(greet(
    date=datetime.datetime(2021, 5, 7, 12, 0, 1),
    name="John"
    ))
```

- Your result should look like this:

```
Good Morning, John!
Good Afternoon, John!
```

###

### Task 4: Packing and unpacking positional arguments

Create a function `sumAll` that gets the sum of all values in different lists. The function will accept any number of lists, each containing a variable amount of integers.

The function should return the sum of all numbers in any of those lists and it must accept **any** number of parameters (use packing).

Then, define the test cases using this code (use unpacking):

```
test1 = [[0, 2, 4, 5]]
test2 = [
    [0, 2, 4, 5],
    [6],
    [0, 2, 4, 5, 1, 4, 3, 2]
]
```

- Your result should look like this:

```
11
38
```

###

### Task 5: Positional and keyword arguments + default values

Create a `pig_latin` function. This function will receive any amount of String objects. For each word in those strings, it should transform the word according to these rules:

- If the word starts with vowel, add `ay` at the end.
- If not, move the first letter to the end and add `ay`

**Example**:

```
Word => Ordway
Apple => Appleay
```

Additionally, the function will accept a **keyword argument** `suffix` that will allow us to change the suffix `ay` into any other of our choice. If we don't specify this argument, it should keep using `ay` (*default argument*).

You will define another **keyword argument** `single` with a Boolean value to indicate the type of output we want.

This output should be a list containing all the strings passed for translation (the positional arguments), unless the `single` argument is set to `True`, in which case it should return a single String object.

*Consider only a, e, i, o and u as vowels.*

*Attention!! The input strings may have more than one word in them, so you will have to split them first and loop through all the words.*

Call the function (using unpacking) with the following test cases:

```
test1_data = ["Word", "Apple"]
test1_config = {}

test2_data = ["Python", "Functions"]
test2_config = {"suffix": "oy"}

test3_data = ["If the word starts with a vowel", "add the suffix to the word"]
test3_config = {"single": True, "suffix": "ep"}
```

- Your result should look like this:

```
['Ordway', 'Appleay']
['Ythonpoy', 'Unctionsfoy']
If the word starts with a vowelay add the suffix to the worday
```
