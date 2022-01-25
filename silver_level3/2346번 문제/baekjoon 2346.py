#baekjoon 2346
#silver level 3
#2022.01.25

n = int(input())
idx = 0
result = []

data = list(map(int, input().split()))
index = [x for x in range(1, n + 1)]

temp = data.pop(idx)
result.append(index.pop(idx))

while data:
    if temp < 0:
        idx = (idx + temp) % len(data)
    else:
        idx = (idx + (temp - 1)) % len(data)
    temp = data.pop(idx)
    result.append(index.pop(idx))

for r in result:
    print(r, end=' ')