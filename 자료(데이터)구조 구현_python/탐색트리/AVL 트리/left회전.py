def rotate_left(self,n):
    x=n.right
    n.right=x.left
    x.left=n
    n.height=max(self.height(n.left),self.height(n.right))+1
    x.height=max(self.height(n.left),self.height(x.right))+1
    return x