#2022.02.04
#baekjoon 11047
#silver level 3

n, k = map(int, input().split())
m = []
num = 0
for i in range(n):
    m.append(int(input()))
for i in range(n - 1, -1, -1):
    if k == 0:
        break
    if m[i] > k:
        continue
    num += k // m[i]
    k %= m[i]
print(num)