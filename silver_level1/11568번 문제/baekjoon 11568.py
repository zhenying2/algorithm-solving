#baekjoon 11568
#2022.02.03
#silver level 1

from itertools import combinations
N=int(input())
cards=list(map(int,input().split()))

pairs=[]
for i in range(2,N):
  pairs.append(list(combinations(cards,i)))

result=[]
for i in range(len(pairs)):
  for j in range(len(pairs[i])):
    if (list(pairs[i][j]) == sorted(pairs[i][j])):
      result.append(list(pairs[i][j]))
print(len(result[len(result)-1]))
