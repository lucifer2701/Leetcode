# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        li=[]
        if not root:
            return None
        return self.preorder(root,li)
    
    def preorder(self,root,li):
        if not root:
            return None
        li.append(root.val)
        self.preorder(root.left,li)
        self.preorder(root.right,li)
        return li