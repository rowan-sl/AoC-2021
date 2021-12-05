with open("input/day-3.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

MOST = -20
LEAST = -10

def get_occurences(lines, col, tie_breaker, operator: MOST | LEAST):
    occurence_of_1 = 0
    occurence_of_0 = 0
    for line in lines:
        char = line[col]
        if char == "0":
            occurence_of_0 += 1
        else:
            occurence_of_1 += 1
    match operator:
        case _ if operator == MOST:
            if occurence_of_1 > occurence_of_0:
                return "1"
            elif occurence_of_0 > occurence_of_1:
                return "0"
            else:
                return tie_breaker
        case _ if operator == LEAST:
            if occurence_of_1 < occurence_of_0:
                return "1"
            elif occurence_of_0 < occurence_of_1:
                return "0"
            else:
                return tie_breaker

def filter(list, pos, val):
    """
    remove all values from list that do not have val at pos
    """
    new_list = []
    for elem in list:
        if elem[pos] == val:
            new_list.append(elem)
    return new_list.copy()

def bit_str_to_int(bit_str: str):
    last = 1
    res = 0
    for char in reversed(bit_str):##so smallest val is at first value not last
        if char == "1":
            res += last
        last *= 2
    return res

def invert_bitstring(bitstring: str):
    return bitstring.replace("0", "a").replace("1", "0").replace("a", "1")

def get_rating(rating: str, input: list):
    tie_breaker: str
    commonness: LEAST | MOST
    match rating:
        case "o2":
            tie_breaker = "1"
            commonness = MOST
        case "co2":
            tie_breaker = "0"
            commonness = LEAST
    remaining = input.copy()
    for i in range(len(input[0])):
        if len(remaining) == 1:
            break
        most = get_occurences(remaining, i, tie_breaker, commonness)
        remaining = filter(remaining, i, most)
    assert len(remaining) == 1
    return remaining[0]

def part_one(input: list):
    input = input.copy()
    gamma = ""
    epsilon = ""

    for i in range(len(input[0])):
        gamma_at_i = get_occurences(input, i, False, MOST)
        epsilon_at_i = invert_bitstring(gamma_at_i)
        gamma += gamma_at_i
        epsilon += epsilon_at_i
    
    return bit_str_to_int(gamma)*bit_str_to_int(epsilon)

def part_two(input: list):
    o2s = get_rating("o2", input)
    co2s = get_rating("co2", input)
    o2 = bit_str_to_int(o2s)
    co2 = bit_str_to_int(co2s)
    return o2*co2

print(part_two(lines))
print(part_one(lines))



