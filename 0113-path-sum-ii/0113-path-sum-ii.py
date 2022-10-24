# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[];path=[]
        def back(node,curSum):
            nonlocal res,path
            if not node:
                return 
            path.append(node.val)
            curSum+=node.val
            if not node.left and not node.right and curSum==targetSum:
                res.append(path[:])
            if node.left:
                back(node.left,curSum)
                path.pop()
            if node.right:
                back(node.right,curSum)
                path.pop()
        back(root,0)
        return res