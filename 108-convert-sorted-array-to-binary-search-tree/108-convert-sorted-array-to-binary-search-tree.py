# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        l=len(nums)
        if not l:   return None
        mid_l=l//2
        return TreeNode(nums[mid_l],self.sortedArrayToBST(nums[:mid_l]),self.sortedArrayToBST(nums[mid_l+1:]))