file = open('day14_test.in', 'r')

input_sequence = file.readline().strip()

rules_dict = {}

letter_set = set()

for line in file.readlines():
	if len(line.strip())>0:
		rules_dict[line.strip().split(" -> ")[0]] = line.strip().split(" -> ")[0][0] + line.strip().split(" -> ")[1] + line.strip().split(" -> ")[0][1]
		letter_set.add(line.strip().split(" -> ")[0][0])
		letter_set.add(line.strip().split(" -> ")[1])
		letter_set.add(line.strip().split(" -> ")[0][1])

#print(input_sequence)
#print(rules_dict)
#print(letter_set)

letter_count_dict = {k:0 for k in sorted(letter_set)}

def code_expansion(input_combo, step):
	if step < 41:
		global letter_count_dict
		global rules_dict
		expanded_combo = rules_dict[input_combo]
		#print("exploring:", input_combo, "step:", step, "expansion:", expanded_combo)
		letter_count_dict[expanded_combo[1]] = letter_count_dict[expanded_combo[1]] + 1

		code_expansion(expanded_combo[:2], step + 1)
		code_expansion(expanded_combo[1:], step + 1)

for i in range(len(input_sequence)-1):
	letter_count_dict[input_sequence[i]] = letter_count_dict[input_sequence[i]] + 1
	code_expansion(input_sequence[i]+input_sequence[i+1], 1)

letter_count_dict[input_sequence[-1]] = letter_count_dict[input_sequence[-1]] + 1

max_number = 0
min_number = 10000000
for key in letter_count_dict:
	if max_number < letter_count_dict[key]:
		max_number = letter_count_dict[key]

	if min_number > letter_count_dict[key]:
		min_number = letter_count_dict[key]

print(max_number - min_number)