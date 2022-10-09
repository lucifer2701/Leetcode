# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        res = False
        diff = set()
        
        def traverse(root):
            nonlocal res, diff
            
            if not res:
                if k - root.val in diff:
                    res = True
                
                else:
                    diff.add(root.val)
                    if root.left:
                        traverse(root.left)
                    if root.right:
                        traverse(root.right)
                        
        traverse(root)
        return res