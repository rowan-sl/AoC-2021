import numpy as np

with open("input/real.txt") as f:
    txt = f.read()

tdots, tfolds = txt.split("\n\n")
dots = set()
for line in tdots.splitlines():
    x, y = line.split(",")
    dots.add((int(x), int(y)))
folds = []
for line in tfolds.splitlines():
    axis, cord = line[11:].split("=")
    folds.append((axis, int(cord)))

for i, fold in enumerate(folds):
    axis, cord = fold
    ndots = set()
    for dot in dots:
        dotx, doty = dot
        match axis:
            case "x":
                dotx = min(dotx, 2*cord - dotx)
            case "y":
                doty = min(doty, 2*cord - doty)
        ndots.add((dotx, doty))
    if i == 0: print(len(ndots))
    dots = ndots

ally = []
allx = []
for dot in dots:
    x, y = dot
    ally.append(y)
    allx.append(x)
maxx = max(allx)
maxy = max(ally)
code = np.zeros((maxx+1, maxy+1))
for dot in dots:
    code[dot] = 1
print(str(code).replace("1.", "N").replace("0.", " "))