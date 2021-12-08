
# The seven segment display is represented like this:
#
#  111
# 2   3
# 2   3
# 2   3
#  444
# 5   6
# 5   6
# 5   6
#  777
#
# each number (input) has a corisponding list of outputs for the display

from typing import List


def repr_display(segments: list) -> str:
    seg_display = """
     111
    2   3
    2   3
    2   3
     444
    5   6
    5   6
    5   6
     777"""
    for i in [1,2,3,4,5,6,7]:
        if i in segments:
            seg_display = seg_display.replace(str(i), "●")
        else:
            seg_display = seg_display.replace(str(i), "◎")

    return seg_display

#number = num of segments used
NUM1 = 2
NUM4 = 4
NUM7 = 3
NUM8 = 7
numbers = {
    2: 1,
    4: 4,
    3: 7,
    7: 8,
}

occurences = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
    0: 0,
}

with open("input/real.txt") as f:
    lines = f.readlines()

inputs = []
for line in lines:
    inp, res = line.split("|")
    inp = inp.strip().split()
    res = res.strip().split()
    inputs.append((inp, res))
[print(i) for i in inputs]

for i in inputs:
    inp, out = i
    for o in out:
        if len(o) in numbers.keys():
            num = numbers[len(o)]
            occurences[num] += 1

print(occurences)
print("Summing occurences")
print(sum(occurences.values()))
