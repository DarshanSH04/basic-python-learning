import re
str = input("Enter string: ")
print("Original: ", str)
print("After: ")
def removing(text): return re.sub('[a-z]', '', text)


res = removing(str)
print(res)
