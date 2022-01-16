file = open('day13.in', 'r')

coordinates_string, instruction_string = file.read().strip().split("\n\n")

coordinates_set = set(coordinates_string.split("\n"))
instruction_list = [k.split("fold along ")[1] for k in instruction_string.split("\n")]

for fold in instruction_list:
	folded_set = set()
	axis, fold_coordinate = fold.split("=")
	if axis == 'y':
		for coordinate in coordinates_set:
			if int(coordinate.split(",")[1])<int(fold_coordinate):
				folded_set.add(coordinate)
			else:
				folded_set.add(coordinate.split(",")[0]+","+str(2*int(fold_coordinate)-int(coordinate.split(",")[1])))

	if axis == 'x':
		for coordinate in coordinates_set:
			if int(coordinate.split(",")[0])<int(fold_coordinate):
				folded_set.add(coordinate)
			else:
				folded_set.add(str(2*int(fold_coordinate)-int(coordinate.split(",")[0]))+","+coordinate.split(",")[1])

	coordinates_set = folded_set

x_max = 0
y_max = 0
for coordinates in coordinates_set:
	if x_max < int(coordinates.split(",")[0]):
		x_max = int(coordinates.split(",")[0])
	if y_max < int(coordinates.split(",")[1]):
		y_max = int(coordinates.split(",")[1])

import numpy as np

code = np.zeros((x_max+1,y_max+1))

for coordinates in folded_set:
	code[int(coordinates.split(",")[0])][int(coordinates.split(",")[1])] = 1

print(code)
# ECFHLHZF
