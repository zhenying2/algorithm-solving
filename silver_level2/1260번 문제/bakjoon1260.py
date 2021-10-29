import sys
input = sys.stdin.readline

#deque -> bfs 사용 위해서
from collections import deque

#정점개수 N, 간선개수 M, 탐색 시작 정점 번호 V
N,M,V=map(int,input().split())

#쌍 저장 리스트 생성
pair=[[]*N for _ in range(N+1)]

#방문 여부 확인 리스트 생성 (dfs, bfs 2개)
visited1=[False]*(N+1)
visited2=[False]*(N+1)

for _ in range(M):
    a,b=map(int,input().split())
    #a에 대응->b원소, b에대응 ->a원소 각 리스트에 교차로 저장
    pair[a].append(b)
    pair[b].append(a)
    pair[a].sort()
    pair[b].sort()

#방문 dfs 정의
def dfs(pair,v,visited):
    #현재 노드를 방문 처리
    visited[v]=True
    print(v, end=" ")
    #현재 노드와 연결된 다른 노드 방문
    for i in pair[v]:
        if not visited[i]:
            dfs(pair,i,visited)

#방문 bfs 정의
def bfs(pair,start,visited):
    queue=deque([start])
    #현재 노드를 방문처리
    visited[start]=True
    #큐가 비어있을 때까지 반복
    while queue:
        #큐에서 하나의 원소를 뽑아 출력
        v=queue.popleft()
        print(v,end=" ")
        #해당 원소와 연결된 방문안된 원소 큐에 삽입
        for i in pair[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

dfs(pair,V,visited1)
print()
bfs(pair,V,visited2)
