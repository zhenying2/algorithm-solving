#baekjoon 3078
#gold level 3
#2022.01.26

import sys
input=sys.stdin.readline
N,K=map(int,input().rstrip().split())
students=[]
for i in range(N):
  name=input().rstrip()
  students.append(len(name))

now_index=0
next_index=1
goodfriends=0
for i in range(N):
  while (next_index-now_index <=K):
    if (next_index<N and students[now_index]==students[next_index]):
      goodfriends+=1
      next_index+=1
    else:
      next_index+=1
  now_index+=1
  next_index=now_index+1

print(goodfriends)
  