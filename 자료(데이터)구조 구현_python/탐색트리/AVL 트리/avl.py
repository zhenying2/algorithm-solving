class Node:
    def __init__(self,key,value,height,left=None,right=None):
        self.key=key
        self.value=value
        self.height=height
        self.left=left
        self.right=right

class AVL:
    def __init__(self):
        self.root=None

    def height(self,n):
        if n == None:
            return 0

        return n.height

    def put(self,key,value): #삽입연산
        self.root=self.put_item(self.root,key,value)

    def put_item(self,n,key,value):
        if n == None:
            return Node(key, value,1)

        if n.key>key:
            n.left=self.put_item(n.left,key,value)

        elif n.key<key:
            n.right=self.put_item(n.right,key,value)

        else:
            n.value=value
            return n

        n.height=max(self.height(n.left),self.height(n.right))+1
        return self.balance(n)

    def balance(self,n): #불균형처리
        if self.bf(n) > 1 : #노드 n에서 불균형발생
            if self.bf(n.left)<0:
                n.left=self.rotate_left(n.left)

            n=self.rotate_right(n)

        elif self.bf(n) < -1:
            if self.bf(n.right) >0:
                n.right=self.rotate_right(n.right)

            n=self.rotate_left(n)

        return n

    def bf(self,n): #bf 계산
        return self.height(n._left)-self.height(n._right)

    def rotate_right(self,n): #우로 회전
        x=n.left
        n.left=x.right
        x.right=n
        n.height=max(self.height(n.left),self.height(n.right))+1
        x.height=max(self.height(n.left),self.height(x.right))+1
        return x
    
    def rotate_left(self,n): #좌로 회전
        x=n.right
        n.right=x.left
        x.left=n
        n.height=max(self.height(n.left),self.height(n.right))+1
        x.height=max(self.height(n.left),self.height(x.right))+1
        return x
