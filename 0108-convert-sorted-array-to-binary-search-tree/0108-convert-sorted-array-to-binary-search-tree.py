# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        x=len(nums)
        if x==0:    return None
        y=x//2
        return TreeNode(nums[y],self.sortedArrayToBST(nums[:y]),self.sortedArrayToBST(nums[y+1:]))