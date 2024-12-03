import re

with open("inputs/day3_input.txt") as f:
    memory = f.read()

def part_one():
    matches = re.findall(r"mul\((\d+),(\d+)\)", memory)
    print(matches)
    solution = sum(int(x)*int(y) for (x,y) in matches)
    print(solution)

def part_two():
    matches = re.findall(r"(do\(\)|don't\(\))|mul\((\d+),(\d+)\)", memory)
    print(matches)
    count = True
    solution = 0
    for method,x,y in matches:
        if method=="do()":
            count = True
        elif method=="don't()":
            count = False
        elif x and y and count:
            solution += int(x)*int(y)
    print(solution)

part_two()