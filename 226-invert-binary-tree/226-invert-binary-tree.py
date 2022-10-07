# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(dummy):
            if dummy:
                temp=dummy.left
                dummy.left=dummy.right
                dummy.right=temp
                if dummy.left:
                    invert(dummy.left)
                if dummy.right:
                    invert(dummy.right)
        invert(root)
        return root