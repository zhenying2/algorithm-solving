#baekjoon 2747
#2022.01.18
#bronze level 3

numbers=[0 for _ in range(46)]
numbers[1]=1

for i in range(2,46):
    numbers[i]=numbers[i-1]+numbers[i-2]

test=int(input())
print(numbers[test])
    
