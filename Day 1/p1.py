list = []
left = []
right = []

with open('p1input.txt', 'r') as file:
    for line in file:
        list.append(line.split())

for line in list:
    left.append(line[0])
    right.append(line[1])
    left.sort()
    right.sort()

x = 0
for i in range(len(right)):
    x+=abs(int(left[i])-int(right[i]))

print(left)
print(right)
print(x)