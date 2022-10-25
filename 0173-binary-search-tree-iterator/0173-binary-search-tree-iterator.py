# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.li=[]
        def pre(node,li):
            if not node:    return
            pre(node.left,li)
            self.li.append(node.val)
            pre(node.right,li)
        pre(root,self.li)

    def next(self) -> int:
        return self.li.pop(0)

    def hasNext(self) -> bool:
        if len(self.li)>0:
            return 1
        return 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()