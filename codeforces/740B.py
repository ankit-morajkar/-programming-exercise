# https://codeforces.com/problemset/problem/740/B

first_line_input = input()

number_of_flowers = list(map(int, first_line_input.split(" ")))[0]

number_of_suggestions = list(map(int, first_line_input.split(" ")))[1]

flower_mood_list = list(map(int, input().split(" ")))

sub_array_indices = []

for i in range(number_of_suggestions):
	index_i = list(map(int, input().split(" ")))
	sub_array_indices.append(list(map(lambda x:x-1, index_i)))


#print("number of flowers:", number_of_flowers)
#print("number of mother's suggestions:", number_of_suggestions)
#print("list of flowers: ", flower_mood_list)
#print("sub-arrays-indices: ", sub_array_indices)

final_answer = 0

for suggestion in range(number_of_suggestions):
	#print("suggestion number: ", suggestion)
	suggestion_array_sum = 0
	for sub_array_index in range(sub_array_indices[suggestion][0], sub_array_indices[suggestion][1]+1):
		suggestion_array_sum = suggestion_array_sum + flower_mood_list[sub_array_index]

	#print("suggestion sum: ", suggestion_array_sum)

	if suggestion_array_sum > 0:
		final_answer = final_answer + suggestion_array_sum

print(final_answer)