N = int(input())
memo = []
for _ in range(N):
	memo.append(input())

inc = 1
for i in range(1, N):
	if memo[i-1] > memo[i]:
		inc = 0

des = 1
for i in range(1, N):
	if memo[i-1] < memo[i]:
		des = 0

if inc == 1:
	print("INCREASING")
elif des == 1:
	print("DECREASING")
else :
	print("NEITHER")