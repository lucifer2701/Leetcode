# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def dfs(node,level):
            if node:
                if level>=len(ans):
                    ans.append([])
                ans[level].append(node.val)
                dfs(node.left,level+1)
                dfs(node.right,level+1)
        dfs(root,0)
        res=[]
        for ele in ans:
            res.append(ele[-1])
        return res