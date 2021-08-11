#파이썬 단순연결리스트로 구현한 스택

class Node: #Node 클래스
    def __init__(self,item,link):
        self.item=item
        self.next=link

def push(item):
    global top #전역변수
    global size

    top=Node(item,top)
    size +=1

def peek(): #peek 연산
    if size != 0:
        return top.item

def pop():
    global top
    global size

    if size != 0:
        temp=top.item
        top=top.next #연결리스트에서 top이 참조하던 노드 분리시킴
        size -=1
        return temp

def print_stack():
    print('top -> \t',end="")
    p=top

    while p:
        if p.next != None:
            print(p.item, '-> ',end='')

        else:
            print(p.item, end="")
        
        p=p.next
    print()

top=None
size=0
push('apple')
push('orange')
push('cherry')
print('사과, 오렌지, 체리 push 후:\t',end="")
print_stack()

print('top 항목: ',end="")
print(peek())

push('pear')
print('배 push 후:\t\t',end="")
print_stack()
print('pop 실행: ', pop())
push('grape')
print('pop(), 포도 push 후:\t',end='')
print_stack()
