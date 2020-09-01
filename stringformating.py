# general
import datetime
person = {
    'name': 'Darshan',
    'age': 21
}
sentence = "My name is " + person['name'] + \
    " and my age is " + str(person['age'])
# print(sentence)

# placeholders
sentence1 = "My name is {} and my age is {}".format(
    person['name'], person['age'])  # placeholders can be numbered like {0} and {1}
# print(sentence1)

# fields of dictionary in placeholders
sentence2 = "My name is {0[name]} and my age is {1[age]}".format(
    person, person)
# print(sentence2)

sentence3 = "My name is {name} and my age is {age}".format(
    name='Darshan', age='21')
# print(sentence3)
# unpacking dictionary

sentence4 = "My name is {name} and my age is {age}".format(**person)
# print(sentence4)

# formating using padding
# for i in range(1, 11):
# print("Value is {:03}".format(i))

pi = 3.14159265
# print("Pi = {:.4f}".format(pi))

# print("Adding commas {:,}".format(1000*1549))

# dates
my_date = datetime.datetime(1999, 7, 11, 12, 5)
# print(my_date)
# print("{:%B %d ,%Y}".format(my_date))
print("{0:%B %d ,%Y} falls on {0:%A} and is {0:%j} day of the year".format(my_date))
