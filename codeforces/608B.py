a = input()
b = input()

answer = 0

#Brute Force
'''
number_of_combos = len(b)-len(a)+1
b_substrings = list()

for i in range(number_of_combos):
	start_index = i
	end_index = i + len(a)
	sub_b = b[start_index:end_index]
	b_substrings.append(sub_b)

for sub_b in b_substrings:
	for i in range(len(a)):
		if a[i]!=sub_b[i]:
			answer += 1

print(answer)
'''

for a_i in range(len(a)):
	for b_i in range(a_i,len(b)-len(a)+a_i+1):
		if a[a_i]!=b[b_i]:
			answer += 1

print(answer)
