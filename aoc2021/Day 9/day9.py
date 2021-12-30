import numpy as np

file = open('day9.in', 'r')

lava_tube_input = [line for line in file.readlines()]

coordinates_array = np.zeros((100,100))
check_grid = np.zeros((100,100))

sum = 0

# Initializing Numpy
for i in range(100):
    i_tube_1 = list(lava_tube_input[i].strip())
    i_tube_2 = list(map(int, i_tube_1))
    for j in range(100):
        coordinates_array[i][j] = i_tube_2[j]

# Part 1

# Solving Corners 
if ((coordinates_array[0][0]<coordinates_array[0][1]) and (coordinates_array[0][0]<coordinates_array[1][0])):
    check_grid[0][0] = 1
    
if ((coordinates_array[0][99]<coordinates_array[0][98]) and (coordinates_array[0][99]<coordinates_array[1][99])):
    check_grid[0][99] = 1
    
if ((coordinates_array[99][0]<coordinates_array[99][1]) and (coordinates_array[99][0]<coordinates_array[98][0])):
    check_grid[99][0] = 1
    
if ((coordinates_array[99][99]<coordinates_array[99][98]) and (coordinates_array[99][99]<coordinates_array[98][99])):
    check_grid[99][99] = 1
    

# Top Edge(without corners)
for i in range(1,99):
    if ((coordinates_array[0][i]<coordinates_array[0][i-1]) 
        and (coordinates_array[0][i]<coordinates_array[0][i+1]) 
        and (coordinates_array[0][i]<coordinates_array[1][i])):
        check_grid[0][i] = 1

# Bottom Edge(without corners)
for i in range(1,99):
    if ((coordinates_array[99][i]<coordinates_array[99][i-1]) 
        and (coordinates_array[99][i]<coordinates_array[99][i+1]) 
        and (coordinates_array[99][i]<coordinates_array[98][i])):
        check_grid[99][i] = 1

# Left Edge(without corners)
for i in range(1,99):
    if ((coordinates_array[i][0]<coordinates_array[i-1][0]) 
        and (coordinates_array[i][0]<coordinates_array[i+1][0]) 
        and (coordinates_array[i][0]<coordinates_array[i][1])):
        check_grid[i][0] = 1

# Right Edge(without corners)
for i in range(1,99):
    if ((coordinates_array[i][99]<coordinates_array[i-1][99]) 
        and (coordinates_array[i][99]<coordinates_array[i+1][99]) 
        and (coordinates_array[i][99]<coordinates_array[i][98])):
        check_grid[i][99] = 1        

# Inner Grid
for i in range(1,99):
    for j in range(1,99):
        if ((coordinates_array[i][j] < coordinates_array[i-1][j]) 
            and (coordinates_array[i][j] < coordinates_array[i+1][j]) 
            and (coordinates_array[i][j] < coordinates_array[i][j-1]) 
            and (coordinates_array[i][j] < coordinates_array[i][j+1])):
            check_grid[i][j] = 1
        
 
for i in range(100):
    for j in range(100):
        if check_grid[i][j] == 1:
            sum = sum + coordinates_array[i][j] + 1
            
#print(sum)
# correct answer

# Part 2

part_2_grid = np.zeros((100,100))

basin_number = 1

for i in range(100):
    for j in range(100):
        if int(coordinates_array[i][j]) == 9:
            part_2_grid = -1

for i in range(100):
    for j in range(100):
        if int(part_2_grid) != -1:
            part_2_grid = -1




















