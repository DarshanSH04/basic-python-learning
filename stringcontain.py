import re


def check_contains(str):
    charre = re.compile(r'[^a-zA-Z0-9]')
    str = charre.search(str)
    return not bool(str)


x = input('Enter the string')
print(check_contains(x))
