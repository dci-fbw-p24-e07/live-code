# File I/O

## Description

In this exercise, we will focus on opening files for reading and practicing the use of the position.

##

## Tasks

###

### Task 1

Open the file [src/data/task1.txt](src/data/task1.txt) and print its entire content with the least amount of instructions possible.

> Make sure the file is closed before the script finishes.

- Your result should look like this:

```
CHAPTER I

JONATHAN HARKER'S JOURNAL

(_Kept in shorthand._)
```

###

### Task 2

Output the amount of ToDos written in the file [src/data/task2.txt](src/data/task2.txt).

> Consider the following:
> - There will always be two lines at the beginning of the list (one with the header and the other empty).
> - Every ToDo in the list will be written in a single line.
> - Every line in the list will contain a single ToDo.
> - There will be nothing after the list.

- Your result should look like this:

```
5
```

###

### Task 3

Open the file [src/data/task3.txt](src/data/task3.txt) and print its entire content as you did on **Task 1**. You will see a text that seems mixed up:

```
_3 May. Bistritz._--Left Munich at 8:35 P. M., on 1st May, arriving at
late and would start as near the correct time as possible. The
Vienna early next morning; should have arrived at 6:46, but train was an
impression I had was that we were leaving the West and entering the
hour late. Buda-Pesth seems a wonderful place, from the glimpse which I
East; the most western of splendid bridges over the Danube, which is
got of it from the train and the little I could walk through the
here of noble width and depth, took us among the traditions of Turkish
streets. I feared to go very far from the station, as we had arrived
rule.
```

This text has been manipulated so that it only reads well if we print the `odd` lines first and then the `even` lines. Write some Python code that opens this file and prints first the `odd` lines and then the `even` lines.

- Your result should look like this:

```
_3 May. Bistritz._--Left Munich at 8:35 P. M., on 1st May, arriving at
Vienna early next morning; should have arrived at 6:46, but train was an
hour late. Buda-Pesth seems a wonderful place, from the glimpse which I
got of it from the train and the little I could walk through the
streets. I feared to go very far from the station, as we had arrived
late and would start as near the correct time as possible. The
impression I had was that we were leaving the West and entering the
East; the most western of splendid bridges over the Danube, which is
here of noble width and depth, took us among the traditions of Turkish
rule.
```

###

### Task 4

Open the file [src/data/task4.txt](src/data/task4.txt) and print the text found between the positions 1622 and 1634 (both included).

- Your result should look like this:

```
the dark side
```

###

### Task 5

Open the file [src/data/task5.txt](src/data/task5.txt) and print the first line and the amount of characters in this line (the line break does not count).

> You are not allowed to use the `len()` function, use the reading position instead.

- Your result should look like this:

```
We left in pretty good time, and came after nightfall to Klausenburgh.

70
```

###

### Task 6

Now open the file [src/data/task6.txt](src/data/task6.txt) and print a list of integers representing the amount of characters per line (with `/n`). The order in the list will be the order of the lines.

> Again, you are not allowed to use the `len()` function.

- Your result should look like this:

```
[70, 72, 72, 68, 70, 66, 68, 72, 70, 71, 71, 73, 73, 19]
```

#

# Disclaimer

The contents are fragments from the book Dracula, *by Bram Stoker*.
