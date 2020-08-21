things = ['mouse','keyboard','laptop','bottle']

print(things) #prints whole list

print(len(things)) # length of list

print(things[2])

print(things[-3]) #goes backwards for -ve indices again

print(things[0:2]) #range of values prints 0th and 1st values only doesn't include 2nd

things.append('book') #adds to last

print(things)

things.insert(2,'paper') # to particular location

print(things)

things_1 = ['speaker','marker']

#things.insert(3,things_1) remove comment and run,comment the next one this will add the whole list to the index for sdding onlu vslues run next one

things.extend(things_1)  

print(things)

things.remove('laptop')
 
print(things)

things.pop() # removes last value and returns it used like a stack 

print(things)

things.reverse() #reversing whole list

print(things)

things.sort()

print(things) # alphabetical order, for numbers its ascending order

things.sort(reverse=True) # descending order

print(things)

# these altar the original list, for the one which won't altar the original list use sorted function assigned to a variable

unaltared_things = sorted(things)

print(unaltared_things)

nums = [3,4,5,2,7,1]

print(nums)

print(min(nums))
print(max(nums))
print(sum(nums))

# to find index of any value
print(things.index('keyboard'))
print('keyboard' in things) #gives true if present else false


for index in things:
	print(index)    # printing using for with newline

for index,thing in enumerate(things):    # enumerates with index default start from 0
	print(index,thing)

for index,thing in enumerate(things,start=1):  # starts from 1
	print(index,thing)

# converting from listd to string 
things_2 = ' - '.join(things)

print(things_2)

# reverse conversion
new_list = things_2.split(' - ')
print(new_list)
