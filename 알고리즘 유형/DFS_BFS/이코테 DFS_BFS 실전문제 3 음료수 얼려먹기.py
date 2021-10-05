#얼음 틀의 세로길이, 가로 길이 입력
N,M=map(int,input().split())

#얼음판 구조 입력
icecase=[]
for _ in range(N):
    icecase.append(list(map(int,input())))
    
#DFS 메서드 정의
def icecream(x,y):
    if x<0 or x>=N or y<0 or y>=M:
        return False

    #현재 노드를 방문 처리
    if icecase[x][y] ==0:
        icecase[x][y]=1
        #현재 노드와 연결된 다른 노드(상,하,좌,우) 재귀적으로 방문
        icecream(x-1,y)
        icecream(x+1,y)
        icecream(x,y-1)
        icecream(x,y+1)
        return True
    
    return False

result=0
for i in range(N):
    for j in range(M):
        if icecream(i,j) == True:
            result +=1

print(result)
