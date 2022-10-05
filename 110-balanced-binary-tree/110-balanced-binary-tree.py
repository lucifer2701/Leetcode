# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans=1
        def height(root):
            nonlocal ans
            if not root:
                return -1
            hl=height(root.left)
            hr=height(root.right)
            if abs(hl-hr)>1:
                ans=0
            return 1+max(hl,hr)
        height(root)
        return ans