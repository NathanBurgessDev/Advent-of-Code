f = open("Day_01/input.txt","r")

line1 = []
line2 = []

for line in f:
    split = line.split()
    line1.append(split[0])
    line2.append(split[1])

line1.sort()
line2.sort()

dist = 0

for val1,val2 in zip(line1,line2):
    dist += abs(int(val1)-int(val2))    

print(dist)