# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        i=0
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break
        else:
            return None
        slow = head
        while slow != fast:
            fast,slow=fast.next,slow.next
        return slow
    
    