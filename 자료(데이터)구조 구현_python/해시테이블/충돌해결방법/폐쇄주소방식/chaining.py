class Chaining:

    class Node:
        def __init__(self,key,data,link):
            self.key=key
            self.data=data
            self.next=link

    def __init__(self,size):
        self.M=size #M: 테이블의 크기
        self.a=[None]*size #해시테이블 a

    def hash(self,key):
        return key % self.M #나눗셈 해시함수

    def put(self,key,data): #삽입연산
        i=self.hash(key) #초기위치
        p=self.a[i]

        while p !=None:
            if key == p.key:
                p.data=data
                return
            
            p=p.next
        
        self.a[i]=self.Node(key,data,self.a[i])

    def get(self, key): #탐색 연산
        i=self.hash(key) #초기위치
        p=self.a[i]

        while p !=None:
            if key == p.key:
                return p.data
            
            p=p.next

        return None