temp_max = 0
max = []

with open('input.txt', mode='r') as f:
    file_content = f.readlines()

    for elem in file_content:
        if elem != '\n':
            temp_max += int(elem[:-1])
        else:
            max.append(temp_max)
            temp_max = 0

max.sort()
print(max)
# enumerate(max)