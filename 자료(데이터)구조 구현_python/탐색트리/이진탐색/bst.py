class Node:
    def __init__(self,key,value,left=None,right=None):
        self.key=key
        self.value=value
        self.left=left
        self.right=right


class BST:
    def __init__(self): #트리 생성자
        self.root=None #트리 루트

    def get(self, key): #탐색 연산
        return self.get_item(self.root,k)

    def get_item(self,n,k):
        if n ==None:
            return None #탐색 실패

        if n.key > k:
            return self.get_item(n.left,k) #왼쪽 서브트리 탐색

        elif n.key < k:
            return self.get_item(n.right,k) #오른쪽 서브트리 탐색

        else:
            return n.value #탐색 성공

    def put(self,key,value): #삽입 연산
        self.root=self.put_item(self.root,key,value)

    def put_item(self,n,key,value): 
        if n == None: 
            return Node(key, value) #새 노드 생성
        
        if n.key > key:
            n.left=self.put_item(n.left,key, value)

        elif n.key < key:
            n.right=self.put_item(n.right,key,value)
        else:
            n.value=value
        
        return n

    def min(self): #최솟값 가진 노드 찾기
        if self.root == None:
            return None
        return self.minimum(self.root)

    def minimum(self,n):
        if n.left == None:
            return n
        return self.minimum(n.left)

    def delete_min(self): #최솟값 삭제
        if self.root==None:
            print('트리가 비어있음')
        
        self.root=self.del_min(self.root)

    def del_min(self,n):
        if n.left == None:
            return n.right

        n.left=self.del_min(n.left)
        return n

    def delete(self,key): #삭제 연산
        self.root=self.del_node(self.root,k)

    def del_node(self,n,k):
        if n==None:
            return None
        
        if n.key>k:
            n.left=self.del_node(n.left,k)

        elif n.key <k:
            n.right=self.del_node(n.right,k)

        else:
            if n.right == None:
                return n.left

            if n.left == None:
                return n.right

            target=n
            n=self.minimum(target.right)
            n.right=self.del_min(target.right)
            n.left=target.left

        return n