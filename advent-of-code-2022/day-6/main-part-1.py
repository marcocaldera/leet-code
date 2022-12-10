# https://adventofcode.com/2022/day/6

result = 0

with open('input.txt', mode='r') as f:
    file_content = f.readlines()[0]

    start_of_packet = []
    for idx, char in enumerate(file_content):
        start_of_packet.append(char)
        unique_set_of_values = list(set(start_of_packet))

        if len(start_of_packet) == len(unique_set_of_values):
            if len(unique_set_of_values) == 4:
                result = idx + 1
                break
        else:
            start_of_packet = start_of_packet[1:]

print(result)