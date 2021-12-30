
file = open('day7.in', 'r')

input_array = list(map(int, [line for line in file.readlines()][0].split(",")))

# print(min(input_array))
# 0

# print(max(input_array))
# 1955

# Part 1
min_fuel = 500000

for position in range(1956):
    total_fuel = 0

    for crab in input_array:
        total_fuel = total_fuel + abs(crab - position)
        if total_fuel > min_fuel:
            continue
            
    if min_fuel>total_fuel:
        min_fuel = total_fuel
    
# print(min_fuel)

# Part 2

def sum_of_i(i):
    x = 0
    for y in range(i+1):
        x = x + y
        
    return x
    
sum_of_i_dictionary = {}
for i in range(1956):
    sum_of_i_dictionary[i] = sum_of_i(i)


min_fuel = 500000000

for position in range(1956):
    total_fuel = 0

    for crab in input_array:
        total_fuel = total_fuel + sum_of_i_dictionary[abs(crab - position)]
        if total_fuel > min_fuel:
            continue
            
    if min_fuel>total_fuel:
        min_fuel = total_fuel
        
print(min_fuel)
