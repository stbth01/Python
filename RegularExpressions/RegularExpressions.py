import re

name = raw_input("Enter file:")
if len(name) < 1 : name = "regex_sum_42.txt"
hand = open(name)

total = 0

for line in hand:
    line = line.rstrip()
    stgValue = re.findall('[0-9]+', line)
    for num in stgValue:
        total += int(num)

print(total)
