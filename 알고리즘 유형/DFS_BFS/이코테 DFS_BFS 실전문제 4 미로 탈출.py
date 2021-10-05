from collections import deque

#미로의 세로길이, 가로 길이 입력
N,M=map(int,input().split())

#미로 구조 입력
maps=[]
for _ in range(N):
    maps.append(list(map(int,input())))

#이동할 네 방향
dx=[-1,1,0,0]
dy=[0,0,-1,1]

#BFS 메서드 정의
def go(x,y):
    queue=deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            # 미로 구조에서 벗어난 경우
            if nx <0 or nx>= N or ny<0 or ny>=M:
                continue

            #벽 괴물인 경우
            if maps[nx][ny] ==0:
                continue

            if maps[nx][ny] ==1:
                maps[nx][ny]=maps[x][y]+1
                queue.append((nx,ny))
    return maps[N-1][M-1]

print(go(0,0))
