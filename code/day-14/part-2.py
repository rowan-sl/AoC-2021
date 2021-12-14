with open("input/real.txt") as f:
    txt = f.read()
    sequence, rules = txt.split("\n\n")
sequence = sequence.strip()
trules = rules.strip().splitlines()
rules = []
for line in trules:
    sect, char = line.split(" -> ")
    rules.append((sect, char))


occurences = {}
print(len(sequence))
print(sequence)
for i, char in enumerate(sequence):
    if i+1 == len(sequence):
        break
    nchar = sequence[i+1]
    key = char+nchar
    if key not in occurences.keys():
        occurences[key] = 1
    else:
        occurences[key] += 1

def incrementdefault(dinput, key, val):
    if key in dinput.keys():
        dinput[key] += val
    else:
        dinput[key] = val

print(occurences)

for i in range(40):
    noccurences = {}
    for seq in occurences.keys():
        occ = occurences[seq]
        for rule in rules:
            if seq == rule[0]:
                pair1 = seq[0]+rule[1]
                pair2 = rule[1]+seq[1]
                incrementdefault(noccurences, pair1, occ)
                incrementdefault(noccurences, pair2, occ)
                break
        else:
            incrementdefault(noccurences, seq, occ)
    print(noccurences)
    occurences = noccurences.copy()

loccurences = {}
for i in occurences.keys():
    num = occurences[i]
    for ch in i:
        if ch in loccurences.keys():
            loccurences[ch] += num
        else:
            loccurences[ch] = num

least = None
most = None
for i in loccurences.keys():
    occ = loccurences[i]
    if least is None:
        least = (i, occ)
    else:
        if least[1] > occ:
            least = (i, occ)
    if most is None:
        most = (i, occ)
    else:
        if most[1] < occ:
            most = (i, occ)

print(loccurences)
print(least, most)
#le black magic
print(int(most[1]/2-least[1]/2))
