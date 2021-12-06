import tqdm
import time

with open("input/day-6.txt") as f:
    text = f.read()

numbers = text.split(",")
ungrouped_fishies = [int(i) for i in numbers]
grouped_fishies = [0]*9
for fish in ungrouped_fishies:
    grouped_fishies[fish] += 1

days = 1000000


s = time.time()

for i in tqdm.trange(days, unit="days"):
    evolved_fishies = [0]*9
    for fish_state, fish_count in enumerate(grouped_fishies):
        if fish_state == 0:
            evolved_fishies[8] += fish_count
            evolved_fishies[6] += fish_count
        else:
            evolved_fishies[fish_state-1] += fish_count

    grouped_fishies = evolved_fishies

e = time.time()

total = 0
for fish in grouped_fishies:
    total += fish
print(total)
print(f"finished in {e-s}")