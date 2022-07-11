# 2022.07.11

import sys

def hanoi(n,a,b,c):
    if n==1:
        print(a,c)
        return
    hanoi(n-1,a,c,b)
    print(a,c)
    hanoi(n-1,b,a,c)

count=0
N=int(sys.stdin.readline())

for i in range(N):
    count=count*2+1
print(count)
hanoi(N,1,2,3)