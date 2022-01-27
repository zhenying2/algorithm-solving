#baekjoon 1182
#2022.01.27
#silver level 2

from itertools import combinations

N,S=map(int,input().split())
hubo=list(map(int,input().split()))
index=[i for i in range(N)]
pairs=[]
for i in range(1,N+1):
  pairs.append(list(combinations(index,i)))

counts=0
for i in range(len(pairs)):
  for j in range(len(pairs[i])):
    sums=0
    for k in range(len(pairs[i][j])):
      sums+=hubo[pairs[i][j][k]]
    if (sums == S):
      counts+=1

print(counts)