import re

with open('p2input.txt', 'r') as file:
    data = file.read()

# Define the regex pattern for valid mul instructions and do/don't (no idea how this works)
# mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
# do_pattern = r"do\(\)"
# dont_pattern = r"don't\(\)"

# ChatGPT teaches that I should define a single regex pattern to capture all instructions
alex_pattern = r"(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))"

# Find all matches, preserving order
alex = re.finditer(alex_pattern, data)

# alex = re.findall(mul_pattern, data)
# do_m = re.findall(do_pattern, data)
# dont_m = re.findall(do_pattern, data)

total = 0
enabled = True

for match in alex:
    instruction = match.group(0)

    if instruction == "do()":
        enabled = True
    elif instruction == "don't()":
        enabled = False
    else:
        if enabled:
            # for x, y in alex:
                # total += int(x) * int(y)
            x, y = map(int, match.groups()[1:])
            total += x * y

print(total)