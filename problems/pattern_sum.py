# Find the sum of all the numbers present in the below string:
# '''anc34bx 56 234 qwert12 dskcndn678fdk'''
# 34 + 56 + 234 + 12 + 678

# string . split (' ') = list - iternate over items - item -> substring('regex pattern') = sum = 0 ; value + sum = value = sum

import re

sum = 0
pattern = r"[0-9]+"

string = 'anc34bx 56 234 qwert12 dskcndn678fdk'
numList = string.split(' ')
print(numList)

values = []

for item in numList:
    values.append(re.findall(pattern, item)[0])
    
for val in values:
    sum = sum + int(val)

print(sum)
