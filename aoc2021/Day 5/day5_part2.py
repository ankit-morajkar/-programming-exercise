#Part 2

import numpy as np

file = open('day5.in', 'r')

input_array = [line for line in file.readlines()]
len(input_array)
#500

# min coordinate = 10
# max coordinate = 990

coordinates_array = np.zeros((500,4))
grid = np.zeros((1000, 1000))

number_overlapping_points = 0

for i in range(500):
    a = input_array[i].strip().split(" ")
    coordinates_array[i][0] = int((a[0].split(","))[0])
    coordinates_array[i][1] = int((a[0].split(","))[1])
    coordinates_array[i][2] = int((a[2].split(","))[0])
    coordinates_array[i][3] = int((a[2].split(","))[1])
    
    if (coordinates_array[i][0] == coordinates_array[i][2]):
        if (coordinates_array[i][1] < coordinates_array[i][3]):
            for j in range(int(coordinates_array[i][1]), int(coordinates_array[i][3])+1):
                grid[int(coordinates_array[i][0])][j] = grid[int(coordinates_array[i][0])][j]+1
                
        if (coordinates_array[i][1] > coordinates_array[i][3]):
            for j in range(int(coordinates_array[i][3]), int(coordinates_array[i][1])+1):
                grid[int(coordinates_array[i][0])][j] = grid[int(coordinates_array[i][0])][j]+1
        
    elif (coordinates_array[i][1] == coordinates_array[i][3]):
        if (coordinates_array[i][0] < coordinates_array[i][2]):
            for j in range(int(coordinates_array[i][0]), int(coordinates_array[i][2])+1):
                grid[j][int(coordinates_array[i][1])] = grid[j][int(coordinates_array[i][1])]+1
                
        if (coordinates_array[i][0] > coordinates_array[i][2]):
            for j in range(int(coordinates_array[i][2]), int(coordinates_array[i][0])+1):
                grid[j][int(coordinates_array[i][1])] = grid[j][int(coordinates_array[i][1])]+1
                
    elif abs(coordinates_array[i][2]-coordinates_array[i][0]) == abs(coordinates_array[i][3]-coordinates_array[i][1]):
        if (coordinates_array[i][0] < coordinates_array[i][2]):
            if (coordinates_array[i][1] < coordinates_array[i][3]):
                x = 0
                while (x<=abs(coordinates_array[i][2]-coordinates_array[i][0])):
                    grid[int(coordinates_array[i][0])+x][int(coordinates_array[i][1])+x] = grid[int(coordinates_array[i][0])+x][int(coordinates_array[i][1])+x] + 1
                    x = x+1
            
            else:
                x = 0
                while (x<=abs(coordinates_array[i][2]-coordinates_array[i][0])):
                    grid[int(coordinates_array[i][0])+x][int(coordinates_array[i][1])-x] = grid[int(coordinates_array[i][0])+x][int(coordinates_array[i][1])-x] + 1
                    x = x+1
                    
        else:
            if (coordinates_array[i][1] < coordinates_array[i][3]):
                x = 0
                while (x<=abs(coordinates_array[i][2]-coordinates_array[i][0])):
                    grid[int(coordinates_array[i][0])-x][int(coordinates_array[i][1])+x] = grid[int(coordinates_array[i][0])-x][int(coordinates_array[i][1])+x] + 1
                    x = x+1
            
            else:
                x = 0
                while (x<=abs(coordinates_array[i][2]-coordinates_array[i][0])):
                    grid[int(coordinates_array[i][0])-x][int(coordinates_array[i][1])-x] = grid[int(coordinates_array[i][0])-x][int(coordinates_array[i][1])-x] + 1
                    x = x+1
        
        
    
for i in range(1000):
    for j in range(1000):
        if grid[i][j]>1:
            number_overlapping_points = number_overlapping_points + 1
    
    
print(number_overlapping_points)
# Correct Answer
