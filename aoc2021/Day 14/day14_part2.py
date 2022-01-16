import collections

file = open('day14.in', 'r')

input_sequence, rules_string = file.read().strip().split("\n\n")

rules_dict = {}

for rule in rules_string.splitlines():
	src, dst = rule.split(" -> ")
	rules_dict[src] = dst

pair_counts = collections.Counter()

for i in range(len(input_sequence)-1):
	pair_counts[input_sequence[i]+input_sequence[i+1]] += 1

for step in range(40):
	new_counts = collections.Counter()
	char_counts = collections.Counter()
	for k,v in pair_counts.items():
		new_counts[k[0]+rules_dict[k]] += v
		new_counts[rules_dict[k]+k[1]] += v

		char_counts[k[0]] +=v
		char_counts[rules_dict[k]] += v

	pair_counts = new_counts

char_counts[input_sequence[-1]] += 1

vals = sorted(char_counts.values())
print(vals[-1]-vals[0])