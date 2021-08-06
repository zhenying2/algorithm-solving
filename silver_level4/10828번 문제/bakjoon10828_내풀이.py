import sys

#명령의 수 입력받음
count=int(sys.stdin.readline())

stack=[]
for _ in range(count):
    #명령 입력
    order=sys.stdin.readline().strip()
  
    #명령어가 pop이라면
    if (order == 'pop'):
        #stack에 원소가 없다면
        if (len(stack) == 0):
            print(-1)

        #stack에 원소가 있다면
        else:
            print(stack[len(stack)-1])
            del stack[len(stack)-1]
    
    #명령어가 size라면
    elif (order == 'size'):
        print(len(stack)) #스택에 있는 원소 개수 출력

    #명령어가 empty라면
    elif (order == 'empty'):
        #스택이 비어있다면
        if (len(stack)==0):
            print(1)
        
        #스택이 비어있지 않다면
        else:
            print(0)
    
    #명령어가 top이라면
    elif (order == 'top'):
        #스택에 정수가 없다면
        if (len(stack)==0):
            print(-1)
        
        #스택에 정수가 있다면
        else:
            print(stack[len(stack)-1]) #스택의 가장 위 정수 출력
    
    #명령어가 push라면
    else:
        sample=list(order.split())
        stack.append(int(sample[len(sample)-1])) #스택에 원소 삽입
    
