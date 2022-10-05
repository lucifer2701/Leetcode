class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        dummy = TreeNode(0, root, None)

        if depth == 0:
            return root

        def rec(node, depth):
            if node is None:
                return
            if depth == 1:
                node.left = TreeNode(val, node.left, None)
                node.right = TreeNode(val, None, node.right)
                return
            rec(node.left, depth - 1)
            rec(node.right, depth - 1)

        rec(dummy, depth)
        return dummy.left