import numpy as np

file = open('day15.in', 'r')

input_string = file.readlines()

n_rows = len(input_string)
n_cols = len(input_string[0].strip())

input_grid = np.full((n_rows+2, n_cols+2), -1)
final_path = np.full((n_rows+2, n_cols+2), np.inf)

final_path[1][1] = 0

for r in range(n_rows):
	for c in range(n_cols):
		input_grid[r+1][c+1] = int(list(input_string[r].strip())[c])

#print(input_grid)

def adjacent_caves(current_cave, prev_cave):
	adj = []
	if input_grid[current_cave[0]-1][current_cave[1]] != -1:
		adj.append([current_cave[0]-1, current_cave[1]])
	if input_grid[current_cave[0]+1][current_cave[1]] != -1:
		adj.append([current_cave[0]+1, current_cave[1]])
	if input_grid[current_cave[0]][current_cave[1]-1] != -1:
		adj.append([current_cave[0], current_cave[1]-1])
	if input_grid[current_cave[0]][current_cave[1]+1] != -1:
		adj.append([current_cave[0], current_cave[1]+1])

	try:
		adj.remove(prev_cave)
	except:
		pass

	return adj

def enter_cave(current_cave, prev_cave):
	#print("cuurently in:", current_cave)
	adj = adjacent_caves(current_cave, prev_cave)
	global final_path
	final_path[current_cave[0]][current_cave[1]] = final_path[prev_cave[0]][prev_cave[1]]+input_grid[current_cave[0]][current_cave[1]]
	for cave in adj:
		if final_path[cave[0]][cave[1]]>final_path[current_cave[0]][current_cave[1]]+input_grid[cave[0]][cave[1]]:
			enter_cave(cave, current_cave)

enter_cave([1,1], [1,1])

print(final_path[n_rows][n_cols]-1)