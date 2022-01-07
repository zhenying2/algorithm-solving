#baekjoon 1929
#2022.01.07
#time over

#M과 N 입력
M,N=map(int,input().split())
print(N,M)

#M이상 N이하의 소수 출력
for i in range(M,N+1):
    for j in range(2, i):
        if (i % j ==0): #현재 자신의 수 미만에서 나눠 떨어지는 수 있는 경우 -> 소수 아님
            break
        #for문 이후에, 자신 미만에서 나눠 떨어지는 수 없음 -> 소수
        #위 if문 먼저 돌고 아래의 if문을 실행하므로 나머지 0인 것에 대한 조건 걸 필요 없음
        if (j == i-1):
            print(i)
