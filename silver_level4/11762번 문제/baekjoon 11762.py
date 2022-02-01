#2022.02.01
#baekjoon 11762
#silver level 4

from itertools import combinations
import sys
import collections

input=sys.stdin.readline
inputs=list(map(int,input().rstrip().split()))
#tower
towers=inputs[6:]
#box
boxes=inputs[:6]
pairs=list(combinations(boxes,3))
result1=[]
result2=[]
for i in range(len(pairs)):
  if (sum(pairs[i])==towers[0]):
    for j in range(3):
      result1.append(pairs[i][j])
    result2=list(set(boxes)-set(result1))
    break
result1.sort(reverse=True)
result2.sort(reverse=True)
result1.extend(result2)
for k in range(len(result1)):
  print(result1[k],end=" ")