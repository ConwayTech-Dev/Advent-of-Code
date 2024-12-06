list = []
left = []
right = []

with open('p2input.txt', 'r') as file:
    for line in file:
        list.append(line.split())

for line in list:
    left.append(line[0])
    right.append(line[1])

left.sort()
right.sort()

# --

counts = {}

result = []

for element in left:
    if element in right:
        counts[element] = right.count(element)

for element, count in counts.items():
    print(element, ":", count)
    x = left.count(element)
    result.append(int(element)*int(count)*int(x))

list_sum = sum(result)

print(list_sum)