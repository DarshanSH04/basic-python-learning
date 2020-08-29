# lists
from operator import attrgetter
li = [6, 8, 4, 5, 2, 1, 3, 7]
print(li)

# ascending order
# sorted creates/returns new list and doesn't change original
li_1 = sorted(li)
print(li_1)

print(li)
li.sort()
print(li)

# descending order
li_2 = sorted(li, reverse=True)
print(li_2)

print(li)
li.sort(reverse=True)
print(li)

# tuples
tup = (6, 8, 4, 5, 2, 1, 3, 7)
print(tup)

tup_1 = sorted(tup)
print(tup_1)
# sort() method doesn't work for tuple as it changes the original tuple which is contradicting to tuple's rules

# dictionary
di = {'Name': 'Darshan', 'Age': '20', 'Gender': 'M'}
print(di)
di_1 = sorted(di)
print(di_1)

# class


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({}, {}, {})'.format(self.name, self.age, self.salary)


e1 = Employee('Sage', 21, 50000)
e2 = Employee('Omen', 25, 11552)
e3 = Employee('Jett', 19, 59415)

employees = [e1, e2, e3]


def e_sort(emp):
    return(emp.salary)


s_employees = sorted(employees, key=e_sort)  # can use reverse = TRUE
print(s_employees)

# using lamda
s_employees1 = sorted(employees, key=lambda e: e.name)
print(s_employees1)

# using attrgetter

s_employees2 = sorted(employees, key=attrgetter('salary'))
print(s_employees2)
