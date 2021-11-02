import sys
input=sys.stdin.readline

#첫번째 줄에 N,K가 공백으로 구분되어 입력
N,K=map(int,input().split())

#배열 A의 원소들이 공백으로 입력
A=list(map(int,input().split()))
A.sort() #바꿔치기 위해 순서대로 작-> 큰 순으로 배열


#배열 B의 원소들이 공백으로 입력
B=list(map(int,input().split()))
B=sorted(B,reverse=True) #바꿔치기 위해 역순으로 큰-> 작 순으로 배열

count=0 #바꾸는 횟수 세는 변수
#A의 원소들이 최대가 되도록 배열
for i in range(N):
    for j in range(N):
        if A[i] < B[j] and count <K :
            count+=1
            A[i], B[j]=B[j],A[i]

#A의 원소 합 출력
print(sum(A))
