# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x1=[]
        x2=[]
        lis=[]
        x3=res=ListNode(0)
        while l1:
            x1.append(int(l1.val))
            l1=l1.next
        while l2:
            x2.append(int(l2.val))
            l2=l2.next
        x1.reverse()
        x2.reverse()
        sx1=''
        sx2=''
        for i in range(len(x1)):
            sx1+=str(x1[i])
        for i in range(len(x2)):
            sx2+=str(x2[i])
        s=str(int(sx1)+int(sx2))
        for i in range(len(s)):
            lis.append(int(s[i]))
        lis.reverse()
        for ele in lis:
            x3.next=ListNode(ele)
            x3=x3.next
        return res.next