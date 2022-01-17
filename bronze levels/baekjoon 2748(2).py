#baekjoon 2748
#2022.01.17

n=int(input())

numbers=[0]*(n+1)
numbers[1]=1

for i in range(2,n+1):
    numbers[i]=numbers[i-1]+numbers[i-2]

print(numbers[n])
