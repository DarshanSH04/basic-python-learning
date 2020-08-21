message = 'Hello World'

print(message[0:5])

print(message[6:])

print(message.lower())

print(message.upper())

print(message.count('l')) #for counting how many times the argument exists in the string

print(message.count('Hello'))

print(message.find('World'))

print(message.find('hi')) #negative when it can't find

print(message.replace('World','Universe')) #2 arguments first for what's to be replaced and second for new string

a='Hello'

name = 'Darshan'

greeting = a + ', ' + name
print(greeting)

formating = '{}, {}. Welcome!'.format(a,name) #place holder in string
print(formating)

format1 = f'{a.upper()}, {name}. Welcome!'     # f strings formating only for python 3.6 and above, useful to code inside like a.upper
print(format1)

#print(dir(name))___prints all attributes that can be used over that particular argument
#print(help(str))___printd description about that classin argument
