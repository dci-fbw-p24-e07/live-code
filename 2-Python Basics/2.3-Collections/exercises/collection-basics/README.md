# Collections Basics 1

This group of exercises focuses on getting a hands-on feel for lists and their syntax. The tasks will repeat how to:

- Create a list with data
- Append and remove elements
- Loop over a list's elements

## Usage

Lists can be stored in variables just like Strings can. For example to store a list of car brands you could create a variable `car_brands` with a list of brands like `'BMW'`, `'Audi'`, and `'Volkswagen'`. This translates to the following code:

```python
car_brands = ['BMW', 'Audi', 'Volkswagen']
```

Elements in this list can be accessed by zero-based, numbered indizes. For example `car_brands[0]` would return `BMW`.

To work with all elements in a list you can loop over its elements and for example print them like this:

```python
for brand in car_brands:
  print(brand)
```

Lists can also be altered. Elements can be added using the `append` method:

```python
car_brands.append('Volvo')
```

Using indizes elements can also be removed from a list again using the `pop` method:

```python
car_brands.pop(0)
```

###

## Tasks

###

### Task 1

Create a variable called `fruits` and one after another add the elements `Apples`, `Cherries` and `Strawberries`. Loop over the list `fruits` and print every element to the screen.

- Your result should look like this:

```
Apples
Cherries
Strawberries
```

###

### Task 2

Create a variable `cities` which holds a list with the cities `London`, `Paris`, `Berlin` and `Amsterdam`. Print the sentence `The capital city of Germany is: Berlin` to the screen, using the string `Berlin` from the cities array.

- Your result should look like this:

```
The capital city of Germany is: Berlin
```

###

### Task 3

Store the colors `cyan`, `magenta`, `green`, `yellow`, `black` and `white` in a list called `colors`. Remove the colors `green` and `white`. Print the remaining colors to the screen.

- Your result should look like this:

```
cyan
magenta
yellow
black
```

###

### Task 4

Store the letters `p`, `e`, `n`, `g`, `u`, `i`, `n` in a list. Combine those letters into a single string `penguin`. Capitalize that string and print it to the screen.

- Your result should look like this:

```
Penguin
```
