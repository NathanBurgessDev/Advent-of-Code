from collections import defaultdict
f = open("Day_01/input.txt","r")

line1 = []
line2 = []

for line in f:
    split = line.split()
    line1.append(split[0])
    line2.append(split[1])
    
res = defaultdict(int)

for val in line2:
    res[val] += 1

count = 0
for val in line1:
    count += (res[val] * int(val))
print(count)