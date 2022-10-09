# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, minimum, maxmimum): #helper method -- check if our node 
            if not node: #an empty tree is a valid BST!
                return True
            if not minimum < node.val < maxmimum: #if the node isn't in our valid range
                return False #not a BST
            return validate(node.left, minimum, node.val) and validate(node.right, node.val, maxmimum) #make sure the left and right subtrees are also valid
        return validate(root, float('-inf'), float('inf')) #start with the root which can be any value