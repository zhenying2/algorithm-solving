import sys
input=sys.stdin.readline
N,M=map(int,input().split()) # N*M 크기

board=[]

for _ in range(N):
    board.append(list(map(int,input().strip())))

#왼,오,아래,위
dx=[-1,1,0,0]
dy=[0,0,-1,1]

start=[[0,0]]

while start:
    x,y=start[0][0],start[0][1]

    del start[0]

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if nx>=0 and ny>=0 and nx<N and ny<M:
            if board[nx][ny]==1:
                start.append([nx,ny])
                board[nx][ny]=board[x][y]+1

print(board[N-1][M-1])