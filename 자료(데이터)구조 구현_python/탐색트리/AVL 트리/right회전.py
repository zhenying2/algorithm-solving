def rotate_right(self,n):
    x=n.left
    n.left=x.right
    x.right=n
    n.height=max(self.height(n.left),self.height(n.right))+1
    x.height=max(self.height(n.left),self.height(x.right))+1
    return x
    