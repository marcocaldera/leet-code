# https://adventofcode.com/2022/day/3

sum = 0

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_lowercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()

with open('input.txt', mode='r') as f:
    file_content = f.readlines()

    groups = list(zip(*(iter(file_content),) * 3))
    for group in groups:
        backpack_inventory = {}
        for backpack in group:
            backpack = backpack.replace('\n', '')
            backpack = "".join(set(backpack)) # Remove duplicates

            for item in backpack:
                if item in backpack_inventory:
                    backpack_inventory[item] += 1
                else:
                    backpack_inventory[item] = 1
        
        for item in backpack_inventory:
            if backpack_inventory[item] >= 3:
                if item in alphabet_lowercase:
                    sum += alphabet_lowercase.index(item) + 1
                else:
                    sum += len(alphabet) + alphabet.index(item) + 1

                break

print(sum)