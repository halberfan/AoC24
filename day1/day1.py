import re

with open("inputs/day1_input.txt") as f:
    lines = f.read().split("\n")

left = []
right = []

for line in lines:
    nums = re.findall("[0-9]*[0-9]", line)
    left.append(int(nums[0]))
    right.append(int(nums[1]))

left.sort()
right.sort()

def part_one():
    total_distance = sum(abs(left[i]-right[i]) for i in range(0, len(left)))
    print(f"PART ONE: {total_distance}")

def part_two():
    m = {}
    for n in right:
        if n not in m:
            m.update({n:1})
        else:
            m.update({n:m[n]+1})
    similarity_score = 0
    for n in left:
        if n in m:
            similarity_score += n * m[n]
    print(f"PART TWO: {similarity_score}")

part_one()
part_two()