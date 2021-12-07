from tqdm import trange

with open("input/real.txt") as f:
    txt = f.read()
    sints = txt.split(",")
    ints = [int(i) for i in sints]

def get_fuel(pos, newpos):
    dist = abs(newpos-pos)
    used = 0
    cost = 1
    for i in range(dist):
        used += cost
        cost += 1
    return used

def get_all_fuel(crabpos, newpos):
    total = 0
    for crab in crabpos:
        total += get_fuel(crab, newpos)
    return total

all = []
for i in trange(max(ints)+10):
    all.append(get_all_fuel(ints, i))

print(min(all))