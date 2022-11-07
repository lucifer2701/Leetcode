class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre= None
        while head: head.next, pre, head = pre, head, head.next
        return pre