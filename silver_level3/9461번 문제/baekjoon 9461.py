#baekjoon 9461
#2022.01.17
#정답풀이


#삼각형 변 길이 리스트 형성
numbers=[0]*(101)
numbers[1]=1
numbers[2]=1
numbers[3]=1
for j in range(4,101):
    numbers[j]=numbers[j-2]+numbers[j-3]

N=int(input())
for i in range(N):
    n=int(input())
    print(numbers[n])
