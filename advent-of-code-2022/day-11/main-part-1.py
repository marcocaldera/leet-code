# https://adventofcode.com/2022/day/11
import operator
import copy

monkeys = {}
current_monkey = ''

with open('input.txt', mode='r') as f:
    file_content = f.readlines()

    for instruction in file_content:
        instruction = instruction.replace('\n', '')

        if 'Monkey' in instruction:

            current_monkey = instruction.split(':')[0]
            monkeys[current_monkey] = {}
            
        elif 'Starting items' in instruction:

            items = [int(elem) for elem in instruction.split(':')[-1].split(',') ]
            monkeys[current_monkey]['items'] = items

        elif 'Operation' in instruction:

            operation = instruction.split()[-3:]
            monkeys[current_monkey]['operation'] = operation

        elif 'Test' in instruction:

            divided_by = int(instruction.split('Test:')[-1].split()[-1])
            monkeys[current_monkey]['test'] = divided_by

        elif 'true' in instruction:

            monkey_to_throw = instruction.split('If true: throw to ')[-1]
            monkeys[current_monkey]['throw_to'] = { 'true': monkey_to_throw.title() }

        elif 'false' in instruction:

            monkey_to_throw = instruction.split('If false: throw to ')[-1]
            monkeys[current_monkey]['throw_to']['false'] = monkey_to_throw.title()

############
### GAME ###
############

operators = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.floordiv,
    '%' : operator.mod,
}

round = 0

while round < 20:
    round += 1 
    print('Round: ', round)

    for monkey_name in monkeys:
        monkey = monkeys[monkey_name]
        items = copy.deepcopy(monkey['items'])
        
        # For every item that the 'monkey' has
        for worry_level in items:
          
          # Update number of time a monkey is expecting an element:
          if 'evaluations' in monkey:
              monkey['evaluations'] += 1
          else:
              monkey['evaluations'] = 1


          operation_to_perform = copy.deepcopy(monkey['operation'])

          # Replace 'old' with the current item worry_level
          for idx in range(len(operation_to_perform)):
              if operation_to_perform[idx] == 'old':
                  operation_to_perform[idx] = worry_level

          # Perform operation
          op1, operation, op2 = int(operation_to_perform[0]), operation_to_perform[1], int(operation_to_perform[2])
          new_worry_level = operators[operation](op1, op2)

          # Monkey gets bored with the item. Divide the 'new_worry_level' by 3 and round down
          new_worry_level = operators["/"](new_worry_level, 3)
          
          # Check if current worry level is divisible by 'divided_by'
          divided_by = monkey['test']
          if operators["%"](new_worry_level, divided_by) == 0:
              throw_to = monkey['throw_to']['true']
          else:
              throw_to = monkey['throw_to']['false']
          
          # Add item to the new monkey
          monkeys[throw_to]['items'].append(new_worry_level)
          # Remove item from the current monkey
          monkey['items'].pop()

for monkey in monkeys:
  print(f'{monkey}: {monkeys[monkey]["evaluations"]}')