# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A,B=headA,headB
        a=[]
        b=[]
        ans=ListNode(0)
        while A:
            a.append(A.val)
            A=A.next
        while B:
            b.append(B.val)
            B=B.next
        a.reverse()
        b.reverse()
        c=0
        for i in range(min(len(a),len(b))):
            if a[i]==b[i]:
                c+=1
        x=len(a)-c
        y=len(b)-c
        while x!=0:
            headA=headA.next
            x-=1
        while y!=0:
            headB=headB.next
            y-=1
        while headA and headB:
            if headA==headB:
                ans=headA
                return ans
                headA=headA.next
                headB=headB.next
            else:
                ans=0
                headA=headA.next
                headB=headB.next
        return 