class Node:
    #노드 생성자, 항목과 왼쪽/오른쪽 자식노드 레퍼런스
    def __init__(self,item,left=None,right=None):
        self.item=item
        self.left=left
        self.right=right

class BinaryTree:
    def __init__(self):
        self.root=None
    
    def preorder(self,n): #전위순회
        if n != None:
            print(str(n.item),' ', end="") #맨 먼저 노드를 방문

            if n.left:
                self.preorder(n.left) #왼쪽 서브트리 방문 후
            
            if n.right:
                self.preorder(n.right) #오른쪽 서브트리 방문
    
    def inorder(self,n): #중위순회
        if n != None:
            if n.left:
                self.inorder(n.left) 
            print(str(n.item),' ', end="") #왼쪽 서브트리 방문 후 노드방문

            if n.right:
                self.inorder(n.right)

    def postorder(self,n): #후위순회
        if n != None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(str(n.item),' ', end="") #왼쪽과 오른쪽 서브트리 모두 방문 후에 노드 방문

    def levelorder(self, root): #레벨순회
        q=[]
        q.append(root)

        while len(q) !=0:
            t=q.pop(0) #큐에서 첫 항목 삭제
            print(str(t.item),' ',end="") #삭제된 노드 방문
            if t.left != None:
                q.append(t.left)
            if t.right != None:
                q.append(t.right)
    
    def height(self, root): #트리의 높이 계산
        if root == None:
            return 0
        return max(self.height(root.left), self.height(root.right))+1 #두 자식노드 높이중 큰높이 +1 (높이의 시작을 1로 두기 위함 0으로 두면 안더해도 됨 근데 난 1로 시작하고픔)

