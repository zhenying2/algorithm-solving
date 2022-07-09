# 22.07.09

# 1부터 N까지 자연수중에서 중복 없이 M개를 고른 수열 구하는 프로그램

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        dfs()
        s.pop()
        visited[i] = False
            

n, m = map(int, input().split())
s = []
visited = [False] * (n+1)

dfs()
