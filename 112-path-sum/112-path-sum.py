# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int,curSum=0) -> bool:
        if root is None:    return False
        if root.left is None and root.right is None:
            if curSum+root.val==targetSum:  return True
            return False
        ans1=self.hasPathSum(root.left,targetSum,curSum+root.val)
        ans2=self.hasPathSum(root.right,targetSum,curSum+root.val)
        return ans1 or ans2