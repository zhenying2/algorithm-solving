class CircleList:
    #노드 생성자
    #item(data)와 next(link=레퍼런스)로 구성
    class Node:
        def __init__(self,item,link):
            self.item=item
            self.next=link
    

    #원형연결리스트 생성자
    #last와 size로 구성
    def __init__(self):
        self.last=None
        self.size=0

    def no_items(self): return self.size
    def is_empty(self): return self.size==0

    def insert(self,item):
        n=self.Node(item,None) #새노드를 n변수가 참조

        #비어있는 원형리스트였다면
        if self.is_empty():
            n.next=n
            self.last=n

        #기존에 item이 있는 원형리스트라면
        else:
            n.next=self.last.next
            self.last.next=n
        
        self.size +=1

    def first(self):
        if self.is_empty():
            raise EmptyError('Underflow')
        
        f=self.last.next
        return f.item
    
    def delete(self):
        if self.is_empty():
            raise EmptyError('Underflow')
        
        x=self.last.next

        if self.size ==1:
            self.last = None #empty 리스트가 된다
        
        else:
            self.last.next=x.next

        self.size -=1
        return x.item

    def print_list(self):
        if self.is_empty():
            print('리스트가 비어있음')
        else:
            f=self.last.next
            p=f
            while p.next != f: #첫노드를 다시 방문하기 전까지 반복
                print(p.item, ' -> ', end="")
                p=p.next
            
            print(p.item)


#에러 발생시 에러처리 코드
class EmptyError(Exception):
    pass

