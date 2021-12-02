from collections import namedtuple

with open("input/in1.txt", "r") as f:
    lines = f.readlines()

inputs = []
for l in lines:
    parts = l.strip().split(" ")
    inputs.append(parts)

horizontal = 0
depth = 0
aim = 0

for act in inputs:
    amnt = int(act[1])
    match act[0]:
        case "forward":
            horizontal += amnt
            depth += aim*amnt
        case "up":
            aim -= amnt
        case "down":
            aim += amnt
    print(act[0], amnt, horizontal, depth)

print("done")
print(horizontal, depth)
print("answer")
print(horizontal*depth)