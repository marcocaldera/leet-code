# https://adventofcode.com/2022/day/3

sum = 0

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_lowercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()

with open('input.txt', mode='r') as f:
    file_content = f.readlines()

    for elem in file_content:
        backpack_inventory_1 = {}
        string_len = len(elem)
        elem = elem.replace('\n', '')
        elem = [c for c in elem]

        half = int(string_len / 2)

        compartment_1, compartment_2 = elem[0 : half], elem[half : string_len]

        for item in compartment_1:
            if item in backpack_inventory_1:
                backpack_inventory_1[item] += 1
            else:
                backpack_inventory_1[item] = 1
            
        
        for item in compartment_2:
            if item in backpack_inventory_1:

                if item in alphabet_lowercase:
                    sum += alphabet_lowercase.index(item) + 1
                else:
                    sum += len(alphabet) + alphabet.index(item) + 1

                break
                    

print(sum)