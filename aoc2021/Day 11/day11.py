import numpy as np

file = open('day11.in', 'r')

octopus_input = [line for line in file.readlines()]

sum_of_flashes = 0

octopus_array = np.full((12,12), -1)
#print("octopus_array 1st: ", octopus_array)

for i in range(1, 11):
	octopus_row = list(map(int, octopus_input[i-1].strip()))
	#print("octopus_row: ", octopus_row)
	for j in range(1,11):
		#print("Octopus element:", octopus_row[j-1])
		octopus_array[i][j] = octopus_row[j-1]

def flash(octopus_array, source_i, source_j, sum_of_flashes):
	sum_of_flashes = sum_of_flashes + 1
	# Top Left
	if octopus_array[source_i-1][source_j-1] > 0 and octopus_array[source_i-1][source_j-1] < 9:
		octopus_array[source_i-1][source_j-1] = octopus_array[source_i-1][source_j-1] + 1

	elif octopus_array[source_i-1][source_j-1] == 9:
		octopus_array[source_i-1][source_j-1] = 0
		#print("Flashing", source_i-1, source_j-1)
		octopus_array, sum_of_flashes = flash(octopus_array, source_i-1, source_j-1, sum_of_flashes)

	# Top
	if octopus_array[source_i-1][source_j] > 0 and octopus_array[source_i-1][source_j] < 9:
		octopus_array[source_i-1][source_j] = octopus_array[source_i-1][source_j] + 1

	elif octopus_array[source_i-1][source_j] == 9:
		octopus_array[source_i-1][source_j] = 0
		#print("Flashing", source_i-1, source_j)
		octopus_array, sum_of_flashes = flash(octopus_array, source_i-1, source_j, sum_of_flashes)

	# Top Right
	if octopus_array[source_i-1][source_j+1] > 0 and octopus_array[source_i-1][source_j+1] < 9:
		octopus_array[source_i-1][source_j+1] = octopus_array[source_i-1][source_j+1] + 1

	elif octopus_array[source_i-1][source_j+1] == 9:
		octopus_array[source_i-1][source_j+1] = 0
		#print("Flashing", source_i-1, source_j+1)
		octopus_array, sum_of_flashes = flash(octopus_array, source_i-1, source_j+1, sum_of_flashes)

	# Left
	if octopus_array[source_i][source_j-1] > 0 and octopus_array[source_i][source_j-1] < 9:
		octopus_array[source_i][source_j-1] = octopus_array[source_i][source_j-1] + 1

	elif octopus_array[source_i][source_j-1] == 9:
		octopus_array[source_i][source_j-1] = 0
		#print("Flashing", source_i, source_j-1)
		octopus_array, sum_of_flashes = flash(octopus_array, source_i, source_j-1, sum_of_flashes)

	# Right
	if octopus_array[source_i][source_j+1] > 0 and octopus_array[source_i][source_j+1] < 9:
		octopus_array[source_i][source_j+1] = octopus_array[source_i][source_j+1] + 1

	elif octopus_array[source_i][source_j+1] == 9:
		octopus_array[source_i][source_j+1] = 0
		#print("Flashing", source_i, source_j+1)
		octopus_array, sum_of_flashes = flash(octopus_array, source_i, source_j+1, sum_of_flashes)

	# Bottom Right
	if octopus_array[source_i+1][source_j-1] > 0 and octopus_array[source_i+1][source_j-1] < 9:
		octopus_array[source_i+1][source_j-1] = octopus_array[source_i+1][source_j-1] + 1

	elif octopus_array[source_i+1][source_j-1] == 9:
		octopus_array[source_i+1][source_j-1] = 0
		#print("Flashing", source_i+1, source_j-1)
		octopus_array, sum_of_flashes = flash(octopus_array, source_i+1, source_j-1, sum_of_flashes)

	# Bottom
	if octopus_array[source_i+1][source_j] > 0 and octopus_array[source_i+1][source_j] < 9:
		octopus_array[source_i+1][source_j] = octopus_array[source_i+1][source_j] + 1

	elif octopus_array[source_i+1][source_j] == 9:
		octopus_array[source_i+1][source_j] = 0
		#print("Flashing", source_i+1, source_j)
		octopus_array, sum_of_flashes = flash(octopus_array, source_i+1, source_j, sum_of_flashes)

	# Bottom Right
	if octopus_array[source_i+1][source_j+1] > 0 and octopus_array[source_i+1][source_j+1] < 9:
		octopus_array[source_i+1][source_j+1] = octopus_array[source_i+1][source_j+1] + 1

	elif octopus_array[source_i+1][source_j+1] == 9:
		octopus_array[source_i+1][source_j+1] = 0
		#print("Flashing", source_i+1, source_j+1)
		octopus_array, sum_of_flashes = flash(octopus_array, source_i+1, source_j+1, sum_of_flashes)

	#print("New Flash", source_i, source_j, "\n", octopus_array)
	return octopus_array, sum_of_flashes

# Part 1
'''
for day in range(1, 101):
	flashed_array = np.zeros((12,12))
	visited_array = np.zeros((12,12))
	# Update the Octopus level for the day
	for i in range(1,11):
		for j in range(1,11):
			if octopus_array[i][j]<9:
				octopus_array[i][j] = octopus_array[i][j] + 1

			else:
				octopus_array[i][j] = 0
				flashed_array[i][j] = 1

	#print("day", day, "initial octopus array\n", octopus_array)
	#print("day", day, "flashed octopi\n", flashed_array)
	# For all the octopi flashed today, update the neighbours
	for i in range(1,11):
		for j in range(1,11):
			if flashed_array[i][j] == 1:
				#print("Flashing", i, j)
				octopus_array, sum_of_flashes = flash(octopus_array, i, j, sum_of_flashes)

print("final flashes:", sum_of_flashes)
'''

# Part 2
day =1 
while day > 0:
	#print(octopus_array)
	tot_flashed_today = 0
	flashed_array = np.zeros((12,12))
	# Update the Octopus level for the day
	for i in range(1,11):
		for j in range(1,11):
			if octopus_array[i][j]<9:
				octopus_array[i][j] = octopus_array[i][j] + 1

			else:
				octopus_array[i][j] = 0
				flashed_array[i][j] = 1

	#print("day", day, "initial octopus array\n", octopus_array)
	#print("day", day, "flashed octopi\n", flashed_array)
	# For all the octopi flashed today, update the neighbours
	for i in range(1,11):
		for j in range(1,11):
			if flashed_array[i][j] == 1:
				#print("Flashing", i, j)
				octopus_array, sum_of_flashes = flash(octopus_array, i, j, sum_of_flashes)

	for i in range(1,11):
		for j in range(1,11):
			if octopus_array[i][j] == 0:
				tot_flashed_today = tot_flashed_today + 1

	if tot_flashed_today == 100:
		#print(octopus_array)
		break

	day = day + 1	

print("all flashed day:", day)