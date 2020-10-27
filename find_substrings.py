import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
frequency = 0
for m in re.findall(pattern, text):
    print('Found "%s"' % m)
    frequency += 1
print("Frequency: ", frequency)
