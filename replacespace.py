import re
str = "Python exercises, PHP exercises"
print(re.sub(r'[ ,.]', ":", str, 2))
