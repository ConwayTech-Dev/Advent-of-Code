import re

with open('p1input.txt', 'r') as file:
    data = file.read()

# Define the regex pattern for valid mul instructions and do/don't (no idea how this works)
mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
do_pattern = r"do\(\)"
dont_pattern = r"don't\(\())"

alex = re.findall(mul_pattern, data)
do_m = re.findall(do_pattern, data)
dont_m = re.findall(do_pattern, data)

total = 0

for x, y in alex:
    total += int(x) * int(y)

print(total)