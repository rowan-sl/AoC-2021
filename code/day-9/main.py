import numpy as np
import re
from math import prod
import networkx as nx

with open("input/real.txt") as f:
    RAW = f.read()

HEIGHTMAP: np.ndarray = np.fromiter(map(int, re.findall(r"\d", RAW)), dtype=int).reshape(100, 100)

PADDED_HEIGHTMAP: np.ndarray = np.pad(HEIGHTMAP, 1, mode="constant", constant_values=10)

trisk = 0

for i in range(1, 101):
    for j in range(1, 101):
        at = PADDED_HEIGHTMAP[i, j]
        left = PADDED_HEIGHTMAP[i, j-1]
        right = PADDED_HEIGHTMAP[i, j+1]
        up = PADDED_HEIGHTMAP[i+1, j]
        down = PADDED_HEIGHTMAP[i-1, j]
        if (
            (at < left) and
            (at < right) and
            (at < up) and
            (at < down)
        ):
            trisk += at+1

print(trisk)


cave_map = nx.grid_graph((100, 100))
lines = RAW.splitlines()
for i, line in enumerate(lines):
    for j, val in enumerate(line):
        cave_map.nodes[i, j]["height"] = int(val)

to_remove = []
for node in cave_map:
    if cave_map.nodes[node]["height"] == 9:
        to_remove.append(node)

cave_map.remove_nodes_from(to_remove)

connected = nx.connected_components(cave_map)
sizes = [len(n) for n in connected]
largest = sorted(sizes)[-3:]

print(prod(largest))
