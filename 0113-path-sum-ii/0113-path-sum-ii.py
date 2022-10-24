# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        path = []
        def back(node,cur_sum):
            nonlocal path,res
            if not node:
                return
            path.append(node.val)
            cur_sum+=node.val
            if not node.left and not node.right and cur_sum==targetSum:
                res.append(path[:])
            if node.left:
                back(node.left,cur_sum)
                path.pop()
            if node.right:
                back(node.right,cur_sum)
                path.pop()
            
        back(root,0)
        
        return res