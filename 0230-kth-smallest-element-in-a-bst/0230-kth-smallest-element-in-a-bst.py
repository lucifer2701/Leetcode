# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        li=[]
        def trav(node,li):
            if not node:    return
            trav(node.left,li)
            li.append(node.val)
            trav(node.right,li)
        trav(root,li)
        return li[k-1]