#baekjoon 9461
#2022.01.17
#index error

N=int(input())

for i in range(N):
    n=int(input())
    numbers=[0]*(n+1)
    numbers[1]=1
    numbers[2]=1
    numbers[3]=1
    for j in range(4,n+1):
        numbers[j]=numbers[j-2]+numbers[j-3]

    print(numbers[n])
