class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:        
        
        def merge(root1, root2):
            if root1 is None:
                return root2
            if root2 is None:
                return root1
            return TreeNode(root1.val + root2.val,merge(root1.left, root2.left),merge(root1.right, root2.right))
        
        return merge(root1, root2)