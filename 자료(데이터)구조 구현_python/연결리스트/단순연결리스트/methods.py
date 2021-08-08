class SimpleList:
    
    class Node:
        #노드의 생성자, 노드의 데이터와 링크를 선언+정의
        def __init__(self,item,link):
            self.item=item
            self.next=link

    #단순연결리스트 생성자, head와 항목의 크기로 구성
    def __init__(self):
        self.head=None
        self.size=0

    def size(self): return self.size
    def is_empty(self): return self.size == 0

    def insert_front(self,item):
        if self.is_empty(): #empty라면
            self.head=self.Node(item,None)

        else:
            #기존 head가 가리키는 link를 새 노드의 link도 가리킨다
            #기존 head가 새롭게 만든 node를 가리킨다 
            self.head=self.Node(item,self.head)
        
        self.size +=1
    
    def insert_after(self, item, p):
        p.next=self.Node(item,p.next)
        self.size +=1
    
    def delete_front(self):
        if self.is_empty(): #empty라면
            raise EmptyError('Underflow') #에러처리
        else:
            self.head=self.head.next
            self.size -=1
        
    def delete_after(self, p):
        if self.is_empty(): #empty라면
            raise EmptyError('Underflow') #에러처리
        
        t=p.next
        p.next=t.next
        self.size -=1

    def search(self, target):
        p=self.head #head부터 순차탐색
        for k in range(self.size):
            if target == p.item : return k #탐색 성공
            p=p.next
        
        return None #탐색 실패

    def print_list(self):
        p=self.head
        while p:
            if p.next != None:
                print(p.item, ' -> ',end='')
            else:
                print(p.item)
            
            p=p.next
        
class EmptyError(Exception): #underflow(empty)시 에러처리
    pass