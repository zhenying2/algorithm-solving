#baekjoon 11000
#2022.02.07~08
#gold level 5

import sys
input=sys.stdin.readline
N=int(input().rstrip())

inputs=[]
for i in range(N):
  inputs.append(list(map(int,input().rstrip().split())))
inputs.sort(key=lambda x:x[0])

classes=[]
classes.append(inputs[0])
for i in range(1,N):
  boolean=False
  for j in classes:
    #기존에 있는 강의보다 더 전에 시작
    if (inputs[i][1]<=j[0]):
      boolean=True
      j[0]=inputs[i][0]
      break
    #기존 강의 이후에 강의 시작
    elif (inputs[i][0]>=j[1]):
      boolean=True
      j[1]=inputs[i][1]
      break
  if (not boolean):
    classes.append(inputs[i])
    

print(len(classes))