import re


def check_match(str):
    pattern = 'ab*?'
    if re.search(pattern, str):
        return "Found match"
    else:
        return "Not found"


print(check_match("c"))
print(check_match("aabbbb"))
print(check_match("abbb"))
print(check_match("abbc"))
