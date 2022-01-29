#baekjoon 21734
#2022.01.29
#bronze level 2

import sys
input=sys.stdin.readline
strs=input().rstrip()

#길이 자리수 합
lengths=[]
for i in range(len(strs)):
  temp=str(ord(strs[i]))
  length=0
  for j in range(len(temp)):
    length+=int(temp[j])
  lengths.append(length)
for k in range(len(strs)):
  print(strs[k]*lengths[k])
