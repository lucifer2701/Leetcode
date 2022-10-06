# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def sym(le,ri):
            if not le and not ri:   return 1
            if le and ri:
                if le.val!=ri.val:
                    return 0
                else:
                    return sym(le.right,ri.left) and sym(le.left,ri.right) 
                return 0
        if not root:    return 1
        return sym(root.left,root.right)
        
       