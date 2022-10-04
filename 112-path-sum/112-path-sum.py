# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int,currSum=0) -> bool:
        if not root: return False
        if root.left is None and root.right is None:
            if currSum + root.val == targetSum: return True
            return False
        op1 = self.hasPathSum(root.left, targetSum, (currSum + root.val))
        op2 = self.hasPathSum(root.right, targetSum, (currSum + root.val))
        return op1 or op2