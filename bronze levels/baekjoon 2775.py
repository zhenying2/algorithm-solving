#baekjoon 2775
#bronze level 2
#2022.01.15

case=int(input())

for i in range(case):
    k=int(input())
    n=int(input())
    counts=[i for i in range(1,n+1)]
    for _ in range(k):
        for j in range(1,n):
            counts[j]+=counts[j-1]
            
    print(counts[n-1])
