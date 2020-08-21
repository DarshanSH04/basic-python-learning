students = {'Name': 'Darshan', 'Age': 21}
print(students['Name'])
print(students.get('Age'))
print(students.get('Phone'))
students['Phone'] = '654251'
print(students.get('Phone'))
students.update({'Name': 'dsh', 'Age': 56})
print(students)

del students['Name']
print(students)
age = students.pop('Age')
print(age)
print(len(students))
print(students.values())
print(students.items())
for key in students:
    print(key)
for key in students.items():
    print(key)
