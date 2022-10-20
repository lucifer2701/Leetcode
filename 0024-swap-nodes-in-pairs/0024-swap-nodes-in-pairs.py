# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=head
        while dummy and dummy.next:
            temp=dummy.val
            dummy.val=dummy.next.val
            dummy.next.val=temp
            dummy=dummy.next.next
        return head