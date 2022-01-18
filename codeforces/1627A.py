test_cases = int(input())

answer = []

while test_cases > 0:
	n, m, r, c = list(map(int,input().split(" ")))
	cells = []
	atleast_1_B = False
	same_row_column = False
	for rows in range(n):
		input_row_cell = list(input())
		cells.append(input_row_cell)
		if atleast_1_B == False:
			if input_row_cell.count('B')>0:
				atleast_1_B = True

	if atleast_1_B == False:
		answer.append(-1)

	elif cells[r-1][c-1] == 'B':
		answer.append(0)

	else:
		# Check for the column
		for row_i in range(n):
			if cells[row_i][c-1] == 'B':
				same_row_column = True
				answer.append(1)
				break
		# Check for the row
		if same_row_column == False:
			for col_i in range(m):
				if cells[r-1][col_i] == 'B':
					same_row_column = True
					answer.append(1)
					break

		if same_row_column == False:
			answer.append(2)

	test_cases -= 1

for ans in answer:
	print(ans)