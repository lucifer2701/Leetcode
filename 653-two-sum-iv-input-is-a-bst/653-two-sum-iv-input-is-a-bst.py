# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def existAns(a , b , k):
            if b==None:
                return False
            if a==b:
                return existAns(a,b.left,k) or existAns(a,b.right,k)
            if a.val + b.val == k:
                return True
            if a.val+b.val < k:
                return existAns(a,b.right,k)
            else:
                return existAns(a,b.left,k)
        
        def traverse(root,head, k):
            if (root==None):
                return False
            if existAns(root,head,k):
                return True
            return traverse(root.left,head, k) or traverse(root.right,head, k)
        
        return traverse(root,root,k)
            
        