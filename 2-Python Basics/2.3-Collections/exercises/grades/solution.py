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


def find_passed(students):
    passed = []
    for student in students:
        f_count = 0
        for subject in student["subjects"]:
            if subject["grade"].lower() == 'F'.lower():
                f_count += 1
        
        if f_count < 2:
            passed.append(student)
            
    return passed
    
print(find_passed(students))
