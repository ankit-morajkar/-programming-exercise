import math

def divide_numbers(a, b):
	return (a + b -1)/b

test_cases = int(input())
answer = []

while test_cases>0:
	input_list = list(map(int, input().split(" ")))
	#print(input_list)
	x= input_list[0]
	y= input_list[1]
	k= input_list[2]
	ans = k+ int(math.ceil(divide_numbers(k+k*y-1,x-1)))
	answer.append(ans)
	test_cases = test_cases -1

for ans in answer:
	print(ans)