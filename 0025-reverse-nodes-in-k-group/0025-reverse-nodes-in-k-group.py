class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        groupprev = dummy
        while True :
            kth = self.getKth(groupprev,k)
            if not kth :
                break 
            groupnext = kth.next
            prev , current  = kth.next , groupprev.next
            while current != groupnext :
                Next = current.next
                current.next = prev
                prev = current
                current = Next
            temp = groupprev.next
            groupprev.next = kth
            groupprev = temp
        return dummy.next
    def getKth (self,current : ListNode, k : int)->ListNode :
        while current and k>0 :
            current = current.next
            k-=1
        return current