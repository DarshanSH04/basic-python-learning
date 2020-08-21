a = 12
b = 12
if a == 10:
    print("its 10")
elif a == 11:
    print("its 11")
else:
    print("its not")

a1 = [1, 2, 3]
b1 = [1, 2, 3]

if a1 is b1:
    print("yes")
else:
    print("no")
print(id(a1))
print(id(b1))
