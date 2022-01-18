import collections

test_cases = int(input())

answer = []

for i in range(test_cases):
	answer.append([])
	n, m = list(map(int,input().split(" ")))
	centre = [(n+1)/2, (m+1)/2]
	distance_dict = collections.Counter()
	for r in range(1,n+1):
		for c in range(1,m+1):
			distance_dict[abs(r-centre[0])+abs(c-centre[1])] += 1

	sorted_distances = sorted(distance_dict)
	
	for k in range(n*m):
		distance_dict[sorted_distances[0]] -= 1
		distance = (n/2)+(m/2)-1+sorted_distances[0]
		if distance_dict[sorted_distances[0]] == 0:
			del distance_dict[sorted_distances[0]]
			sorted_distances = sorted(distance_dict)

		answer[i].append(str(int(distance))+" ")

for i in range(test_cases):
	print((''.join(answer[i]))[:-1])
