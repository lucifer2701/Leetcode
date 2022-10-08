# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = root

        # While there is a current node
        while node:

            # If the current node is equal to the value, end the search
            if node.val == val:
                break

            # Else search the left or right subtree
            node = node.left if node.val > val else node.right

        return node