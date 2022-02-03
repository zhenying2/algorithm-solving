#baekjoon 11048
#2022.02.03
#silver level 1

miro = []
N, M = map(int, input().split(' '))
for _ in range(N):
    miro.append(list(map(int, input().split(' '))))

candy = [[0]* (M+1) for _ in range (N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        candy[i][j] = max(candy[i-1][j-1], max(candy[i-1][j], candy[i][j-1]))+miro[i-1][j-1]

print(candy[N][M])
