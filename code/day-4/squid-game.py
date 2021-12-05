import numpy as np

with open("day-4/input/day-4.txt", "r") as f:
    numbers, *txtboards = f.read().split('\n\n')

print(numbers, "\n")

boards = np.loadtxt(txtboards, int).reshape(-1,5,5)

def check_for_win_rows(board):
    for row in board:
        no_win = False
        for elem in row:
            if elem != -50:
                no_win = True
                break
        if not no_win:
            return True
    return False

def has_won(boards):
    winning = []
    for index, board in enumerate(boards):
        board: np.ndarray
        board = board.copy()
        rboard = np.rot90(board)
        if check_for_win_rows(rboard) or check_for_win_rows(board):
            winning.append((board, index))
    return winning

def return_non_winning(boards):
    not_winning = []
    for board in boards:
        board: np.ndarray
        if type(board) == int:
            continue
        board = board.copy()
        rboard = np.rot90(board)
        if not (check_for_win_rows(rboard) or check_for_win_rows(board)):
            not_winning.append(board)
    return not_winning

# for first to win
def get_all_winners():
    all_winners = {}
    # print(has_won(boards))
    for i, snum in enumerate(numbers.strip().split(",")):
        num = int(snum)
        # print(num)
        boards[boards == num] = -50
        winners = has_won(boards)
        for winner in winners:
            board, index = winner
            if index not in all_winners.keys():
                all_winners[index] = (i, board, num)
    return all_winners

winners = get_all_winners()

# print(winners)

print("all boards have won!")
print("getting first and last to win")
min = None
max = None
for winner in winners.values():
    # print(winner)
    if min is None:
        min = winner
    else:
        if min[0] > winner[0]:
            min = winner
    if max is None:
        max = winner
    else:
        if max[0] < winner[0]:
            max = winner

print("first to win")
print(min)
print("last to win")
print(max)

print("Board Complete (first to win):")
print(min)
print(min[2])
print(min)
print("Score")
score = 0
for row in min[1]:
    for elem in row:
        if elem == -50:
            continue
        score += elem
score = score * min[2]
print(score)

print("Board Complete (last to win):")
print(max)
print(max[2])
print(max)
print("Score")
score = 0
for row in max[1]:
    for elem in row:
        if elem == -50:
            continue
        score += elem
score = score * max[2]
print(score)

