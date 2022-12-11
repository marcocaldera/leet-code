# https://adventofcode.com/2022/day/7

directories = {}
visited_paths = {}
current_path = []

def is_bash_command(instruction):
  return instruction.startswith('$')

def is_change_directory(instruction):
  return instruction.startswith('cd')

def is_list_directories(instruction):
  return instruction.startswith('ls')

def is_go_to_root_directory(instruction):
  return instruction.startswith('/')

def is_go_to_previous_directory(instruction):
  return instruction.startswith('..')

def is_showing_directory(instruction):
  return instruction.startswith('dir')

with open('input.txt', mode='r') as f:
    file_content = f.readlines()

    for instruction in file_content:
        instruction = instruction.replace('\n', '')

        if is_bash_command(instruction):
            instruction = instruction.replace("$ ", "")

            if is_change_directory(instruction):
                instruction = instruction.replace("cd ", "")

                if is_go_to_previous_directory(instruction):
                    current_path.pop()
                else:
                    current_path.append(instruction)
            
            elif is_list_directories(instruction):
                continue     
        
        else: # Is result of ls command
            if not is_showing_directory(instruction):
                file_size, file_name = instruction.split(" ")
                file_size = int(file_size)

                # Update folder size up through the current_path
                # Example: current_path: ['/', 'd']
                # iteration-1: update size of: path = '/'
                # iteration-2: update size of: path = '//d'

                for idx in range(len(current_path)):
                    path = "/".join(current_path[:idx + 1])

                    if path in directories:
                        directories[path] += file_size
                    else:
                        directories[path] = file_size



total = 0
for directory in directories:
    if directories[directory] <= 100_000:
        total += directories[directory]

print(total)