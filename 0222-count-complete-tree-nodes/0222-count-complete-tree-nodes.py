# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        li=[]
        if root is None:
            return 0
        def pre(node):
            nonlocal li
            if node is None:
                return
            li.append(node.val)
            pre(node.left)
            pre(node.right)
            return li
        pre(root)
        return len(li)