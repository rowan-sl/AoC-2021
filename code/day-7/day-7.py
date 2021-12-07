from tqdm import trange

with open("input/real.txt") as f:
    txt = f.read()
    sints = txt.split(",")
    ints = [int(i) for i in sints]

def get_fuel(pos, newpos, part):
    dist = abs(newpos-pos)
    #for part 1
    if part == 1:
        return dist
    used = 0
    cost = 1
    for i in range(dist):
        used += cost
        cost += 1
    return used

def get_all_fuel(crabpos, newpos, part):
    total = 0
    for crab in crabpos:
        total += get_fuel(crab, newpos, part)
    return total

def get_answers(part):
    answers = []
    for i in trange(max(ints)+10):
        answers.append(get_all_fuel(ints, i, part))
    return min(answers)

print(get_answers(1))
print(get_answers(2))

