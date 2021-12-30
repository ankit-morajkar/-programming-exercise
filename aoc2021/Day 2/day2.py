# Part 1
file = open('Day 2/day2.in', 'r')

input_array = [line for line in file.readlines()]

input_array

input_array_2 = list(map(lambda s: s.strip(), input_array))

input_array_2

horizontal = 0
vertical = 0

for step in input_array_2:
  instruction = step.split()[0]
  instruction_value = int(step.split()[1])
  if instruction == 'forward':
    horizontal = horizontal + instruction_value
  elif instruction == 'down':
    vertical = vertical + instruction_value
  else:
    vertical = vertical - instruction_value
    
print(horizontal, vertical)

final_solution = horizontal*vertical

print(final_solution)
# Solution is correct

# Part 2

horizontal = 0
vertical = 0
aim = 0

for step in input_array_2:
  instruction = step.split()[0]
  instruction_value = int(step.split()[1])
  if instruction == 'forward':
    horizontal = horizontal + instruction_value
    vertical =vertical + aim*instruction_value
  elif instruction == 'down':
    aim = aim + instruction_value
  else:
    aim = aim - instruction_value
    
print(horizontal, vertical)

final_solution = horizontal*vertical

print(final_solution)