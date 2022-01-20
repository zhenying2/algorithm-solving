#baekjoon 4948
#2022.01.20
#time over

while True:
    n=int(input())

    #n이 0이라면 -> 종료
    if (n == 0):
        break

    if (n ==1):
        print(1)
        continue

    #n이 0이 아니라면 -> n+1~2n 까지 범위 내에서 소수 개수 출력
    count=0
    for i in range(n+1,2*n+1):
        for j in range(2,int(i**0.5)+1):
            if (i % j == 0):
                break
            elif (j==int(i**0.5)):
                count+=1
    print(count)
