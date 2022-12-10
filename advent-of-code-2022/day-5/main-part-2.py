# https://adventofcode.com/2022/day/5


# [S]                 [T] [Q]        
# [L]             [B] [M] [P]     [T]
# [F]     [S]     [Z] [N] [S]     [R]
# [Z] [R] [N]     [R] [D] [F]     [V]
# [D] [Z] [H] [J] [W] [G] [W]     [G]
# [B] [M] [C] [F] [H] [Z] [N] [R] [L]
# [R] [B] [L] [C] [G] [J] [L] [Z] [C]
# [H] [T] [Z] [S] [P] [V] [G] [M] [M]
#  1   2   3   4   5   6   7   8   9 

cargo = {
    '1': ['H', 'R', 'B', 'D', 'Z', 'F', 'L', 'S'],
    '2': ['T', 'B', 'M', 'Z', 'R'],
    '3': ['Z', 'L', 'C', 'H', 'N', 'S'],
    '4': ['S', 'C', 'F', 'J'],
    '5': ['P', 'G', 'H', 'W', 'R', 'Z', 'B'],
    '6': ['V', 'J', 'Z', 'G', 'D', 'N', 'M', 'T'],
    '7': ['G', 'L', 'N', 'W', 'F', 'S', 'P', 'Q'],
    '8': ['M', 'Z', 'R'],
    '9': ['M', 'C', 'L', 'G', 'V', 'R', 'T'],
}

with open('input.txt', mode='r') as f:
    file_content = f.readlines()

    for instruction in file_content:
        instruction = instruction.replace('\n', '')
        move_n, from_, to = instruction.split(' ')[1::2] # [start:stop:step]
        # print(move_n, from_, to)

        cargo_to_move = cargo[from_][-int(move_n):]
        cargo[to] = cargo[to] + cargo_to_move # The only diff from main-part-1

        cargo_from_element_to_keep = len(cargo[from_]) - int(move_n)
        cargo[from_] = cargo[from_][:cargo_from_element_to_keep]

result = ''

for index in cargo:
    result += cargo[index][-1]

print(result)