import sys
input=sys.stdin.readline

#수열에 속해있는 수의 개수 N이 주어진다.
N=int(input())



#입력받은 값 저장 리스트
store=[]
#두번째 줄부터 N+1번째 줄까지 N개의 수가 주어진다.
for _ in range(N):
    a=int(input())
    store.append(a)

#선택 정렬   
for i in range(N):
    for j in range(i,N):
        if store[i] < store[j]:
            store[i],store[j]=store[j],store[i]


#문제에서 원하는 형식으로의 출력
for i in range(N):
    print(store[i], end=" ")
