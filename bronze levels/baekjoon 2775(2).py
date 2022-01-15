#baekjoon 2775
#bronze level 2
#2022.01.15
#time over

def count(k,n):
    counts=0
    
    if (k==0): #0층이라면
        return n
    else: #0층이 아니라면
        for i in range(1,n+1):
            counts+=count(k-1,i)
        return counts
    
case=int(input())

for i in range(case):
    k=int(input())
    n=int(input())
    print(count(k,n))
