# Python logical expressions

## Description

In this exercises, we will practice some more on complex logical expressions.

##

## Tasks

###

### Task 1:

We will now use the following list of users in a blog site:

```
users = [
    {
        "name": "Clark",
        "type": "Publisher",
        "items": [
            {
                "title": "The ABC of Blockchain",
                "status": "Draft",
                "reads": 10
            }
        ]
    },
    {
        "name": "Peter",
        "type": "Publisher",
        "items": []
    },
    {
        "name": "Samantha",
        "type": "Publisher",
        "items": [
            {
                "title": "The ABC of JavaScript",
                "status": "Published",
                "reads": 3254
            },
            {
                "title": "The XYZ of JavaScript",
                "status": "Published",
                "reads": 226
            }
        ]
    },
    {
        "name": "Mathilda",
        "type": "Reviewer",
        "items": [
            {
                "title": "The ABC of Blockchain",
                "status": "Pending"
            }
        ]
    }
]
```

Define a function named `has_hits` with one required parameter as a `String` containing the name of the author we want to query.

The function will return a Boolean (strictly of type `Boolean`) indicating if that author has any hit article.

> An article is a hit if it has more than 1000 reads.

Use the following test cases:

```
print("Clark", has_hits("Clark"))
print("Peter", has_hits("Peter"))
print("Samantha", has_hits("Samantha"))
print("Mathilda", has_hits("Mathilda"))
print("Mario", has_hits("Mario"))
```
- Your result should look like this:

```
Clark False
Peter False
Samantha True
Mathilda False
Mario False
```

###

### Task 2:

Using the same list of users, now define a function named `author_average_reads` with one required parameter as a `String` containing the name of the author we want to query.

The function will return an `Integer` representing the average amount of reads an author has in all its `Published` articles.

> You may use multiple conditionals in `if ... elif ...` structures.

> You will have to take into account that Reviewers' items do not have a "reads" key. Their average amount should be 0.

> You will also have to take into account Authors with an empty list of items.

> And also make sure the function does not return an error if we type the name of an author that does not exist.

> Remember to base the calculation only on the articles with the `status` set to `Published`.

Use the following test cases:

```
print("Clark", author_average_reads("Clark"))
print("Peter", author_average_reads("Peter"))
print("Samantha", author_average_reads("Samantha"))
print("Mathilda", author_average_reads("Mathilda"))
print("Mario", author_average_reads("Mario"))
```
- Your result should look like this:

```
Clark 0
Peter 0
Samantha 1740
Mathilda 0
Mario 0
```

###

### Task 3:

Using the same list of users, now define a function named `author_is_popular` with one required parameter as a `String` containing the name of the author we want to query.

The function will return a `Boolean` (strictly a type `Boolean`) indicating if the average number of reads of all `Published` articles of a particular author is greater than 1000.

> You are NOT allowed to use any `if` conditionals except when checking for the `Published` flag.

> You are not allowed to use the `author_average_reads` function from the previous exercise.


Use the following test cases:

```
print("Clark", author_is_popular("Clark"))
print("Peter", author_is_popular("Peter"))
print("Samantha", author_is_popular("Samantha"))
print("Mathilda", author_is_popular("Mathilda"))
print("Mario", author_is_popular("Mario"))
```
- Your result should look like this:

```
Clark False
Peter False
Samantha True
Mathilda False
Mario False
```
