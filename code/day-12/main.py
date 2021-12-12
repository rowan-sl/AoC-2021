from collections import defaultdict
import os


with open("input/real.txt") as f:
    connections = defaultdict(list)
    for _ in f:
        a, _, b = _.strip().partition("-")
        if b != "start":
            connections[a].append(b)
        if a != "start":
            connections[b].append(a)

def part_1(n:str="start", visited:set=None):
    if visited is None:
        visited = set()
    if n == "end":
        return 1
    if n[0].islower():
        visited.add(n)

    try:
        paths = []
        for c in connections[n]:
            if c not in visited:
                paths.append(part_1(c, visited))
        return sum(paths)
    finally:
        if n[0].islower():
            visited.remove(n)

def part_2(n:str="start", visited:dict={}, visited_small:bool=False):
    if n == "end":
        return 1
    if n[0].islower():
        visited[n] = visited.setdefault(n, 0) + 1

    try:
        length = 0
        for val in connections[n]:
            ss = visited.setdefault(val, 0)
            if ss and visited_small:
                continue
            length += part_2(val, visited, visited_small or ss)
        return length
    finally:
        if n[0].islower():
            visited[n] -= 1

print(part_1())
print(part_2())


