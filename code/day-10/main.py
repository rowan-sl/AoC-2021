from collections import deque

with open("input/real.txt") as f:
    txt = f.read()
lines = txt.strip().splitlines()

OPENING = ["{","[","(","<"]
CLOSING = ["}","]",")",">"]

matches = {
    "(": ")",
    "<": ">",
    "{": "}",
    "[": "]",
}

points = {
    ")": 3,
    ">": 25137,
    "}": 1197,
    "]": 57,
}

comp_points = {
    ")": 1,
    ">": 4,
    "}": 3,
    "]": 2,
}

errscore = 0
autocomp_scores = []

for l, line in enumerate(lines):
    charecters = deque()
    erred = False
    # print("Line", line)
    for char in line:
        # print("char", char)
        if char in OPENING:
            # print("Opening")
            charecters.append(char)
        else:
            # print("closing")
            should_match = matches[charecters.pop()]
            if should_match != char:
                print(f"SyntaxError! expected {should_match}, got {char} on line {l}, worth {points[char]} points")
                errscore += points[char]
                erred = True
    if ((not erred) and (len(charecters) > 0)):
        #no errors, but incomplete
        lscore = 0
        for err in reversed(charecters):
            lscore *= 5
            lscore += comp_points[matches[err]]
        autocomp_scores.append(lscore)

print("\ndone")
print(errscore)
print(autocomp_scores)
print(sorted(autocomp_scores)[int((len(autocomp_scores)-1)/2)])
