import sys
from collections import deque

#명령의 수 입력받음
count=int(sys.stdin.readline())

queue=deque()

for _ in range(count):
    #명령 입력
    order=sys.stdin.readline().strip()
  
    #명령어가 pop이라면
    if (order == 'pop'):
        #큐에 원소가 없다면
        if (len(queue) == 0):
            print(-1)

        #queue에 원소가 있다면
        else:
            print(queue[0])
            del queue[0]
    
    #명령어가 size라면
    elif (order == 'size'):
        print(len(queue)) #큐에 있는 원소 개수 출력

    #명령어가 empty라면
    elif (order == 'empty'):
        #큐가 비어있다면
        if (len(queue)==0):
            print(1)
        
        #큐가 비어있지 않다면
        else:
            print(0)
    
    #명령어가 front라면
    elif (order == 'front'):
        #큐에 정수가 없다면
        if (len(queue)==0):
            print(-1)
        
        #큐에 정수가 있다면
        else:
            print(queue[0]) #큐의 가장 앞 정수 출력
    
    #명령어가 back이라면
    elif (order == 'back'):
        #큐에 정수가 없다면
        if (len(queue)==0):
            print(-1)
        
        #큐에 정수가 있다면
        else:
            print(queue[-1]) #큐의 가장 뒤 정수 출력

    #명령어가 push라면
    else:
        sample=list(order.split())
        queue.append(int(sample[-1])) #큐에 원소 삽입