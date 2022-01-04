import heapq
import math

test_cases = int(input())

# List of Final Answers
final_answer = []

def modInverse(b,m):
    g = math.gcd(b, m)
    if (g != 1):
        # print("Inverse doesn't exist")
        return -1
    else:
        # If b and m are relatively prime,
        # then modulo inverse is b^(m-2) mode m
        return pow(b, m - 2, m)
 
 
# Function to compute a/b under modulo m
def modDivide(a,b,m):
    a = a % m
    inv = modInverse(b,m)
    if(inv == -1):
        return 0
    else:
        return (inv*a) % m

while test_cases > 0:
	final_permutations = 0
	number_of_people = int(input())
	list_of_people = list(map(int, input().split(" ")))

	# Who are the top two speakers?
	largest_speaker = 0
	second_largest_speaker = 0
	for person in list_of_people:
		if person > largest_speaker:
			second_largest_speaker = largest_speaker
			largest_speaker = person
		elif person > second_largest_speaker:
			second_largest_speaker = person

	# Three conditions
	if largest_speaker == second_largest_speaker:
		final_permutations = math.factorial(number_of_people)%998244353
		final_answer.append(final_permutations)

	elif (largest_speaker - second_largest_speaker)>1:
		final_permutations = 0
		final_answer.append(final_permutations)

	else:
		number_of_second_largest_speakers = list_of_people.count(second_largest_speaker)
		# Universe - nC(p+1)*p!*(n-p-1)!
		final_permutations = modDivide(math.factorial(number_of_people)*number_of_second_largest_speakers, number_of_second_largest_speakers+1, 998244353)
		final_answer.append(final_permutations)

	test_cases = test_cases - 1

for answer in final_answer:
	print(answer)
