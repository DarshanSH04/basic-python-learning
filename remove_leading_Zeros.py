import re
ip = "190.08.094.106"
str = re.sub(r"\.[0]*", ".", ip)
print(str)
