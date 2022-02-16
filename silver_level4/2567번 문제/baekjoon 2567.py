#baekjoon 2567
#silver level 4
#2022.02.16

#색종이 수 입력
num=int(input())
#100*100 흰 도화지
array=[[0 for _ in range(101)] for _ in range(101)]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

for _ in range(num):
  x,y=map(int,input().split())
  for i in range(x,x+10):
    for j in range(y,y+10):
      array[i][j]=1

result=0

for i in range(1,101):
  for j in range(1,101):
    if (array[i][j]==1):
      cnt=0
      for k in range(4): 
        nx=i+dx[k]
        ny=j+dy[k]
        if (array[nx][ny]==1): #상하좌우의 칸 탐색
          cnt+=1
      if (cnt==3): #상하좌우 중 3칸이 1로 채워져 있음
        result+=1
      elif (cnt ==2): #상자 모서리
        result+=2
print(result)
      