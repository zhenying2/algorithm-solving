import sys
input = sys.stdin.readline

#컴퓨터의 수 입력
computers=int(input())

#컴퓨터 쌍의 수 입력
pairs=int(input())

#쌍 저장 리스트 생성
#인덱스 번호= 컴퓨터 번호로 맞춰주기 위해 0번째는 []로만 채움
pair=[[]*computers for _ in range(computers+1)]

for _ in range(pairs):
    a,b=map(int,input().split())
    #a에 대응->b원소, b에대응 ->a원소 각 리스트에 교차로 저장
    pair[a].append(b)
    pair[b].append(a)

visited=[False]*(computers+1)

#방문 dfs 정의
def dfs(pair,v,visited):
    global count
    #현재 노드를 방문 처리
    visited[v]=True
    #현재 노드와 연결된 다른 노드 방문
    for i in pair[v]:
        if not visited[i]:
            count+=1
            dfs(pair,i,visited)

count=0

dfs(pair,1,visited)
print(count)
