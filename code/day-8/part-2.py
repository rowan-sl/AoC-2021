def repr_display(segments: list) -> str:
    seg_display = """
     111
    2   3
    2   3
    2   3
     444
    5   6
    5   6
    5   6
     777"""
    for i in [1,2,3,4,5,6,7]:
        if i in segments:
            seg_display = seg_display.replace(str(i), "●")
        else:
            seg_display = seg_display.replace(str(i), "◎")

    return seg_display

# (8 covers all)
#     777
#     222
#     000
#     333
#     555
#     999
# 4059   1472039
# 4059   1472039
# 4059   1472039
#     444
#     222
#     333
#     555
#     999
# 20     1470359
# 20     1470359
# 20     1470359
#    222
#    000
#    333
#    555
#    999

NUM1 = 2#unique
NUM2 = 5
NUM3 = 5
NUM4 = 4#unique
NUM5 = 5
NUM6 = 6
NUM7 = 3#unique
NUM8 = 7#unique
NUM9 = 6

with open("input/example.txt") as f:
    lines = f.readlines()

inputs = []
for line in lines:
    inp, res = line.split("|")
    inp = inp.strip().split()
    res = res.strip().split()
    inputs.append((inp, res))
[print(i) for i in inputs]

def get_common(l1, l2) -> list:
    return list(set(l1) & set(l2))

for i in inputs:
    has_1 = False
    has_4 = False
    has_7 = False
    has_8 = False
    pinputs, out = i
    for inp in pinputs:
        match len(inp):
            case 2:
                has_1 = True
            case 4:
                has_4 = True
            case 3:
                has_7 = True
            case 7:
                has_8 = True
    for a in [has_1, has_7, has_4, has_8]:
        assert a



all_results = []

def get_char(num_len, common_1, common_4):
    match num_len:
        case 2:
            if ((common_1 == 2) and (common_4 == 2)):
                return "1"
        case 3:
            if ((common_1 == 2) and (common_4 == 2)):
                return "7"
        case 4:
            if ((common_1 == 2) and (common_4 == 4)):
                return "4"
        case 5:
            match common_1:
                case 1:
                    match common_4:
                        case 2:
                            return "2"
                        case 3:
                            return "5"
                case 2:
                    if common_4 == 3:
                        return "3"
        case 6:
            match common_1:
                case 2:
                    match common_4:
                        case 3:
                            return "0"
                        case 4:
                            return "9"
                case 1:
                    if common_4 == 3:
                        return "6"
        case 7:
            if ((common_1 == 2) and (common_4 == 4)):
                return "8"
    raise KeyError

for pinput in inputs:
    inps, outs = pinput
    letr_1 = None
    letr_4 = None

    number = ""

    for i in inps:
        match len(i):
            case 2:
                letr_1 = set(i)
            case 4:
                letr_4 = set(i)

    for i in outs:
        char = get_char(
            len(i),
            len(get_common(letr_1, i)),
            len(get_common(letr_4, i)),
        )
        number += char

    all_results.append(int(number))

print("Result:", sum(all_results))
