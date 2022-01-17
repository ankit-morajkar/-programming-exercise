import numpy as np

test_cases = int(input())

answer = [] 

while test_cases>0:
	n = int(input())
	boss_list = list(map(int, input().split(" ")))
	dp = np.full((n+1, 2), np.inf)
	dp[0][0] = 0
	for i in range(0,n):
		for j in range(2):
			skips_here = 0
			if j == 0 and boss_list[i] == 1:
				skips_here = skips_here + 1

			dp[i+1][j^1] = min(dp[i+1][j^1], dp[i][j]+skips_here)

			if i != n-1:
				if j == 0 and boss_list[i+1] == 1:
					skips_here = skips_here + 1

				dp[i+2][j^1] = min(dp[i+2][j^1], dp[i][j]+skips_here)

	answer.append(min(dp[n][0], dp[n][1]))
	test_cases = test_cases - 1

for i in answer:
	print(int(i))

exit(0)