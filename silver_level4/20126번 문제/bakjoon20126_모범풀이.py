import sys

N, M, S = map(int, sys.stdin.readline().split())
timeline = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    timeline.append((x, y))
timeline.sort()
end = 0
for x, y in timeline:
    if x - end < M:
        end = x + y
    else:
        print(end)
        break
else:
    if S - end >= M:
        print(end)
    else:
        print(-1)