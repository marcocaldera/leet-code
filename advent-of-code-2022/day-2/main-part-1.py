# https://adventofcode.com/2022/day/2

alphabet_1 = {'A': 'rock', 'B':'paper', 'C': 'scissors'}
alphabet_2 = {'X': 'rock', 'Y':'paper', 'Z': 'scissors'}
scores = {'X': 1, 'Y': 2, 'Z': 3}
total = 0

with open('input.txt', mode='r') as f:
    file_content = f.readlines()

    for elem in file_content:
        player_1_move, player_2_move = elem.split()
        total += scores[player_2_move]
        
        if alphabet_1[player_1_move] == 'rock' and alphabet_2[player_2_move] == 'scissors':
            continue

        elif alphabet_1[player_1_move] == 'scissors' and alphabet_2[player_2_move] == 'paper':
            continue

        elif alphabet_1[player_1_move] == 'paper' and alphabet_2[player_2_move] == 'rock':
            continue

        elif alphabet_2[player_2_move] == 'rock' and alphabet_1[player_1_move] == 'scissors':
            # win
            total += 6

        elif alphabet_2[player_2_move] == 'scissors' and alphabet_1[player_1_move] == 'paper':
            # win
            total += 6

        elif alphabet_2[player_2_move] == 'paper' and alphabet_1[player_1_move] == 'rock':
            # win
            total += 6

        else:
            # Draw
            total += 3


print(total)
