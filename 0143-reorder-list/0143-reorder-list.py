class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        arr=[]
        curr=head
        while curr:
            arr.append(curr.val)
            curr=curr.next
        curr=head
        i=0
        while curr!=None:
            if i%2==0:
                curr.val=arr.pop(0)
            else:
                curr.val=arr.pop()
            curr=curr.next
            i+=1