import numpy as np

with open("input/day-5.txt", "r") as f:
    txt = f.read()
    lines = txt.splitlines()

segments = []
only_straight = []
for line in lines:
    point1, point2 = line.split(" -> ")
    x1, y1 = point1.split(",")
    x2, y2 = point2.split(",")
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    segments.append(((x1, y1), (x2, y2)))
    if ((x1 == x2) or (y1 == y2)):
        only_straight.append(((x1, y1), (x2, y2)))


def get_direction(p1, p2):
    dir_x: int
    dir_y: int
    if p1[0] > p2[0]:
        dir_x = -1
    elif p1[0] < p2[0]:
        dir_x = 1
    else:
        dir_x = 0

    if p1[1] > p2[1]:
        dir_y = -1
    elif p1[1] < p2[1]:
        dir_y = 1
    else:
        dir_y = 0

    return dir_x, dir_y


def generate_points_for_line(segment):
    pts = []
    directions = get_direction(*segment)
    x = segment[0][0]
    y = segment[0][1]
    ex = segment[1][0]
    ey = segment[1][1]

    while True:
        pts.append((x, y))
        match directions:
            case [1, 0] | [0, 1] | [1, 1]:
                if ((x>=ex) and (y>=ey)):
                    break
            case [-1, 0] | [0, -1] | [-1, -1]:
                if ((x<=ex) and (y<=ey)):
                    break
            case [0, 0]:
                break
            case [-1, 1]:
                if ((x<=ex) and (y>=ey)):
                    break
            case [1, -1]:
                if ((x>=ex) and (y<=ey)):
                    break
            case _:
                print(directions)
                raise ValueError("oopsie")

        x+=directions[0]
        y+=directions[1]

    # print("ex", pts)
    return pts

def get_intersectiions(segments):
    points = {}

    all_points = []
    for seg in segments:
        gen_points = generate_points_for_line(seg)
        all_points.extend(gen_points)

    for point in all_points:
        if point in points.keys():
            points[point] += 1
        else:
            points[point] = 1

    occurences_of_intersection = 0
    for key in points.keys():
        occurences = points[key]
        if occurences > 1:
            occurences_of_intersection += 1
    
    return occurences_of_intersection

print(get_intersectiions(only_straight))
print(get_intersectiions(segments))