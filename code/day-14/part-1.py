from collections import Counter
from tqdm import trange

with open("input/real.txt") as f:
    txt = f.read()
    sequence, rules = txt.split("\n\n")
sequence = sequence.strip()
trules = rules.strip().splitlines()
rules = []
for line in trules:
    sect, char = line.split(" -> ")
    rules.append((sect, char))


for i in trange(10):
    nsequence = ""
    for i, char1 in enumerate(sequence):
        if i+1 == len(sequence):
            nsequence += char1
            break
        char2 = sequence[i+1]
        for rule, insertchar in rules:
            if char1+char2 == rule:
                nsequence += char1+insertchar
                break
        else:
            nsequence += char1
    sequence = nsequence

print(sequence)
c = Counter(sequence)
print(c)
print(c.most_common()[0][1]-c.most_common()[-1][1])