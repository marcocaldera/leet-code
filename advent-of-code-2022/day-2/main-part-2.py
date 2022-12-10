# https://adventofcode.com/2022/day/2

alphabet_1 = {'A': 'rock', 'B':'paper', 'C': 'scissors'}
alphabet_2 = {'X': 'lose', 'Y':'draw', 'Z': 'win'}
scores = {'rock': 1, 'paper': 2, 'scissors': 3}
total = 0

with open('input.txt', mode='r') as f:
    file_content = f.readlines()

    for elem in file_content:
        player_1_move, player_2_move = elem.split()
        
        if alphabet_2[player_2_move] == 'lose':
            total += 0

            if alphabet_1[player_1_move] == 'scissors':
                total += scores['paper']

            elif alphabet_1[player_1_move] == 'paper':
                # win
                total += scores['rock']

            elif alphabet_1[player_1_move] == 'rock':
                # win
                total += scores['scissors']

        elif alphabet_2[player_2_move] == 'draw':
            total += 3
            total += scores[alphabet_1[player_1_move]]

        elif alphabet_2[player_2_move] == 'win':
            total += 6

            if alphabet_1[player_1_move] == 'scissors':
                total += scores['rock']

            elif alphabet_1[player_1_move] == 'paper':
                # win
                total += scores['scissors']

            elif alphabet_1[player_1_move] == 'rock':
                # win
                total += scores['paper']


print(total)
