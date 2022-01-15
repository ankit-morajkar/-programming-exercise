import math

n = int(input())
a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))

reduced_pair = []
num_zeros = 0

for i in range(n):
	if a[i] == 0 and b[i] == 0:
		num_zeros = num_zeros + 1
	elif a[i] == 0:
		pass
	else:
		g = math.gcd(a[i], b[i])
		if a[i] < 0:
			reduced_pair.append([(-1)*int(a[i]/g), (-1)*int(b[i]/g)])
		else:
			reduced_pair.append([int(a[i]/g), int(b[i]/g)])

try:
    highest_freq = reduced_pair.count(max(reduced_pair,key=reduced_pair.count))
except Exception:
    highest_freq = 0

print(highest_freq + num_zeros)