from typing import List
from colors import fmt


with open("input/real.txt") as f:
    txt = f.read()
    lines = txt.strip().splitlines()

class Dumbo:
    def __init__(self, x, y, energy):
        self.x = x
        self.y = y
        self.energy = energy
        self.flashing = False

    def update_energy(self):
        if not self.flashing:
            self.energy += 1
            if self.energy > 9:
                self.energy = 0
                self.flashes()

    def flashes(self):
        self.flashing = True
        positions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        for dx, dy in positions:
            for row in DATA:
                for cell in row:
                    if cell.x == self.x + dx and cell.y == self.y + dy:
                        cell.update_energy()

    def reset_flash(self):
        if self.flashing:
            self.flashing = False
            return 1
        else:
            return 0


DATA = [
    [
        Dumbo(x, y, int(cell))
        for x, cell in enumerate(row)
    ]
    for y, row in enumerate(lines)
]

def display(octopuses: List[List[Dumbo]]):
    res = ""
    for row, rdata in enumerate(octopuses):
        trow = ""
        for col, cdata in enumerate(rdata):
            if cdata.flashing:
                trow += f"{fmt.BGRED}{str(cdata.energy)}{fmt.MRESET}"
            else:
                trow += str(cdata.energy)
        res += trow+"\n"
    return res

def all_same(octopuses: List[List[Dumbo]]):
    for r in octopuses:
        first = r[0]
        for v in r:
            if v.energy != first.energy:
                return False
    return True

flashes = 0
stage = 0
while True:
    stage += 1
    for row, rdata in enumerate(DATA):
        for col, cdata in enumerate(rdata):
            cdata.update_energy()
    print(display(DATA))
    for row, rdata in enumerate(DATA):
        for col, cdata in enumerate(rdata):
            if stage <= 100:
                flashes += cdata.reset_flash()
            else:
                cdata.reset_flash()
    if all_same(DATA):
        break
    print("After stage", stage, "Flashes", flashes, "\n")

print("Part 1", flashes)
print("Part 2", stage)