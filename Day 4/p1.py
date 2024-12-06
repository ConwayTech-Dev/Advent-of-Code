import re

with open("p1input.txt", "r") as file:
    lines = file.split()

cross_x = r"XMAS"

re.finditer(cross_x[0], 10)