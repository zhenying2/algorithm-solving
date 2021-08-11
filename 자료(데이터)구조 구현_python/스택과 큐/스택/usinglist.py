#파이썬 리스트로 구현한 스택

def push(item): #삽입연산
    stack.append(item)

def peek(): #top 항목에 접근
    if len(stack) !=0:
        return stack[-1] #리스트의 맨 뒤 항목을 리턴

def pop(): #반환 후 삭제
    if len(stack) != 0:
        item=stack.pop(-1)
        return item

stack =[]
push('apple')
push('orange')
push('cherry')

print('사과, 오렌지, 체리 push 후: \t',end="")
print(stack, '\t<-top')
print('top 항목: ',end="")
print(peek())
push('pear')
print('배 push 후:\t\t',end="")
print(stack,'\t<- top')

print('pop 실행: ',end="")
print(pop())

push('grape')
print('pop(), 포도 push 후: \t', end="")
print(stack,'\t<- top')