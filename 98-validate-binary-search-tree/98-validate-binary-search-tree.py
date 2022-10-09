# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        li=[]
        if root is None:
            return
        return self.inorder(root,li)
    
    def inorder(self,root,li):
        if root is None :
            return
        self.inorder(root.left,li)
        li.append(root.val)
        self.inorder(root.right,li)
        return self.check(li)
    def check(self,li):
        y=len(li)
        x=sorted(li)
        z=set(li)
        if y!=len(z):   return False 
        if li==x:   return True
        return False