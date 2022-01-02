import heapq
import math

test_cases = int(input())

# List of Final Answers
final_answer = []

while test_cases > 0:
	final_permutations = 0
	number_of_people = int(input())
	list_of_people = list(map(int, input().split(" ")))

	# Who are the top two speakers?
	top_two_speakers = heapq.nlargest(2, list_of_people)
	largest_speaker = top_two_speakers[0]
	second_largest_speaker = top_two_speakers[1]
	number_of_second_largest_speakers = list_of_people.count(second_largest_speaker)

	# Three conditions
	if largest_speaker == second_largest_speaker:
		final_permutations = math.factorial(number_of_people)

	elif (largest_speaker - second_largest_speaker)>1:
		final_permutations = 0

	else:
		# Universe - nC(p+1)*p!*(n-p-1)!
		final_permutations = int(math.factorial(number_of_people) - (
				math.factorial(number_of_people)*
				math.factorial(number_of_second_largest_speakers)/
				(
					math.factorial(number_of_second_largest_speakers + 1)
					)
				))

	final_answer.append(final_permutations%998244353)

	test_cases = test_cases - 1

for answer in final_answer:
	print(answer)