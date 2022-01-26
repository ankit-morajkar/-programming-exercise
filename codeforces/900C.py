total_numbers = int(input())
input_list = list(map(int, input().split(" ")))

def elimination_check(i,j):
	global input_list
	max_i = 0
	unlocked = 0
	for pos in range(j):
		if pos == i:
			pass
		else:
			if input_list[pos]>max_i:
				max_i = input_list[pos]
				if pos > i:
					unlocked += 1

	return unlocked

if total_numbers == 1:
	print(1)

else:
	max_i = 0
	record_pos = []
	max_unlocked = 0
	max_unlocked_numbers = []
	for pos in range(len(input_list)):
		if input_list[pos]>max_i:
			max_i = input_list[pos]
			record_pos.append(pos)

	#print("record position list:", record_pos)
	if len(record_pos)==1:
		if elimination_check(0,len(input_list)) == 1:
			print(1)
		else:
			print(input_list[0])

	elif len(record_pos)==len(input_list):
		print(1)

	else:
		for i in range(len(record_pos)-1):
			unlocked = elimination_check(record_pos[i], record_pos[i+1])
			#print("checking between positions:", record_pos[i], record_pos[i+1], "Unlocked:", unlocked)
			if max_unlocked == unlocked:
				#print("position:", record_pos[i], "unlocked:", unlocked)
				max_unlocked_numbers.append(input_list[record_pos[i]])

			elif max_unlocked < unlocked:
				#print("position:", record_pos[i], "unlocked:", unlocked)
				max_unlocked = unlocked
				max_unlocked_numbers = [input_list[record_pos[i]]]

		unlocked = elimination_check(record_pos[-1], len(input_list)-1)
		if max_unlocked == unlocked:
			max_unlocked_numbers.append(input_list[record_pos[-1]])

		elif max_unlocked < unlocked:
			max_unlocked = unlocked
			max_unlocked_numbers = [input_list[record_pos[-1]]]

		#print("max_unlocked:", max_unlocked, "max_unlocked_numbers:", max_unlocked_numbers)
		if max_unlocked == 1:
			print(1)

		elif max_unlocked == 0:
			for record_pos_i in record_pos:
				#print("deleting:",input_list[record_pos_i])
				input_list[record_pos_i] = 100001
			print(min(input_list))
		else:
			print(min(max_unlocked_numbers))
