import re


def findz(str):
    pattern = r'\Bz\B'
    if re.search(pattern, str):
        return "Found match"
    else:
        return "No match"


print(findz("lazy dog"))
print(findz("dog lazy"))
print(findz("zeolites"))
