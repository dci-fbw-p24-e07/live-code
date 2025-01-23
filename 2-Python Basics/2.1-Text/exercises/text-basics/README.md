# String Basics 1

## Python Texts

In this exercise, we will focus on the use and manipulation of text in Python, including printing special characters, storing text in  variables, and various tools for manipulating text including:

- Using the text concatenation method
- Find the length of a text
- Changing the case of the text

## 

## Usage

A text (also known as String) is a sequence of characters and it is  considered one of the most used data types. A common characteristic of  Strings is that it is immutable, meaning that once created we cannot  change it. From now on we can use both terms interchangeably during this module.

The most common way to use text in Python is to store the textual  data in a variable. The next example demonstrates the creation of a new  variable called `name` in order to store the data `Mary`. To do this, we need to follow the next syntax:

```
name = "Mary"
```

Let's see another example of a phrase:

```
text = "Python is amazing!"
```

We can simply use the `text` variable to extract the required data, for example the next script prints the name `Mary` on the screen.

```
print(name) # In this case I will print the content of the name variable
```

## 

## Tasks

### 

### Task 1

Your task is to create a variable called `city` to store the data: `London` , then print the content of the `city` variable on the screen.

- Your result should look like this:

```
London
```

### 

### Task 2

Your task is to create two variables, the first variable to be called `city` and will store the data: `berlin` , and the second variable to be called `population` and will store the data: `3645000`. Then print the content of the `city` and `population` using a colon (`:`)  in between.  Make sure you capitalize the content of the `city` variable.

- Your result should look like this:

```
Berlin: 3645000
```

### 

### Task 3

Your task is to create two variables, the first variable to be called `city` and will store the data: `london` , and the second variable to be called `population` and will store the data: `9000000`. Then print the content of the `city` and `population` using their labels as shown in the output below. Make sure you check if the content of the `city` is a text. Print the appropriate results on screen as shown bellow.

- Your result should look like this:

```
City: London (True)
Population: 9000000 
```

### 

### Task 4

Create a variable called `text` to store the data: `Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital.` . Your task is to check if  the word `capital`  is included in the text, if so, print the index of the location inside the `text` string.

- Your result should look like this:

```
capital: 92
```

### 

### Task 5

Create a variable called `text` to store the data: `Berlin straddles the banks of the Spree, which flows into the Havel (a tributary of the Elbe) in the western borough of Spandau.` . Your task is to split the content of the `text` variable and store it in a list.

- Your result should look like this:

```
['Berlin', 'straddles', 'the', 'banks', 'of', 'the', 'Spree,', 'which', 'flows', 'into', 'the', 'Havel', '(a', 'tributary', 'of', 'the', 'Elbe)', 'in', 'the', 'western', 'borough', 'of', 'Spandau.']
```

### 

### Task 6

Create a variable called `text` to store the data: `Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital.` . Your task is to replace the word `capital` with the phrase  `capital of Germany` .

- Your result should look like this:

```
Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital of Germany.
```
