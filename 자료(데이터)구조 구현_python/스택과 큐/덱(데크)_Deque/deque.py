from collections import deque

dq=deque('data') #새로운 덱 개체 생성

for i in dq:
    print(i.upper(), end="") #출력: DATA
print()

#dq: d,a,t,a
dq.append('r') #dq: d,a,t,a,r
dq.appendleft('k') #dq: k,d,a,t,a,r
print(dq)

dq.pop() #dq:k,d,a,t,a
dq.popleft() #dq:d,a,t,a
dq.extend('structure')
#dq.extendleft('python') dq: n,o,h,t,y,p,d,a,t,a,s,t,r,u,c,t,u,r,e
dq.extendleft(reversed('python')) #dq: p,y,t,h,o,n,d,a,t,a,s,t,r,u,c,t,u,r,e

print(dq)