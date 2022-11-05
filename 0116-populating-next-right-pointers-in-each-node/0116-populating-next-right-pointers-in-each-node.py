"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        current = leftmost = root
        while current:
            if current.left:
                current.left.next = current.right
            if current.right and current.next:
                current.right.next = current.next.left
            if current.next:
                current = current.next
            else:
                current = leftmost = leftmost.left
        return root