#baekjoon 10250
#2022.01.12
#bronze level 3

#test 데이터 개수 입력
T=int(input())

#test 데이터 입력
for _ in range(T):
    H,W,N=map(int,input().split())
    level=int(N%H)*100+int(N//H)+1
    if (N%H ==0): #N이 H의 배수라면 -> 꼭대기 층 배치
        level=H*100+int(N//H)
    print(level)

