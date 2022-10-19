from collections import Counter
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x=head
        li=[]
        while x:
            li.append(x.val)
            x=x.next
        c=Counter(li)
        temp=[]
        for ele in c:
            if c[ele]==1:
                temp.append(ele)
        temp.sort()
        dummy=ans=ListNode()
        for ele in temp:
            ans.next=ListNode(ele)
            ans=ans.next
        return dummy.next