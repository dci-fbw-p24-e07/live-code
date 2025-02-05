# Task - Sort students by grade

You have a list of students. Each student is made up of a dict containing a key with the name and a list with their subjects. The list of subjects holds dictionaries with the subject name and the grade of the students. If a student has two or more Fs they will need to leave class.

Implement a method that removes the students from the class that have more than two Fs.

## Input:

```python
students = [
  {
    'name': 'Peter', 
    'subjects': [
      {'name': 'English', 'grade': 'A'},
      {'name': 'German', 'grade': 'C'},
      {'name': 'Maths', 'grade': 'B'}
    ]
  },
  {
    'name': 'Robin', 
    'subjects': [
      {'name': 'English', 'grade': 'D'},
      {'name': 'German', 'grade': 'B'},
      {'name': 'Maths', 'grade': 'B'}
    ]
  },
  {
    'name': 'Michael', 
    'subjects': [
      {'name': 'English', 'grade': 'A'},
      {'name': 'German', 'grade': 'F'},
      {'name': 'Maths', 'grade': 'F'}
    ]
  },
]
```

## Output:

```python
students = [
  {
    'name': 'Peter', 
    'subjects': [
      {'name': 'English', 'grade': 'A'},
      {'name': 'German', 'grade': 'C'},
      {'name': 'Maths', 'grade': 'B'}
    ]
  },
  {
    'name': 'Robin', 
    'subjects': [
      {'name': 'English', 'grade': 'D'},
      {'name': 'German', 'grade': 'B'},
      {'name': 'Maths', 'grade': 'B'}
    ]
  },
]
```
