# https://adventofcode.com/2022/day/4

partial_overlaps = 0

with open('input.txt', mode='r') as f:
    file_content = f.readlines()

    for assignments in file_content:
        elf_1_assignment, elf_2_assignment = assignments.split(',')
        
        elf_1_range = [int(x) for x in elf_1_assignment.split('-')]
        elf_1_list = list(range((elf_1_range[0]), elf_1_range[1] + 1))

        elf_2_range = [int(x) for x in elf_2_assignment.split('-')]
        elf_2_list = list(range((elf_2_range[0]), elf_2_range[1] + 1))

        if len(set(elf_1_list) - set(elf_2_list)) < len(elf_1_list):
            partial_overlaps += 1
        elif len(set(elf_2_list) - set(elf_1_list)) < len(elf_2_list):
            partial_overlaps += 1
        elif len(set(elf_1_list) - set(elf_2_list)) == 0 or len(set(elf_2_list) - set(elf_1_list)) == 0:
            partial_overlaps += 1

print(partial_overlaps)