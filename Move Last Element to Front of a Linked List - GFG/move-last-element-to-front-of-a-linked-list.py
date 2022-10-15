from typing import Optional

class Node:
    def __init__(self,x):
        self.data=x
        self.next=None


class Solution:
    def moveToFront(self, head : Optional['Node']) -> Optional['Node']:
        # code here
        slow=head  # Slow pointer

        fast=head.next # Fast pointer -> (slow+1) position

        if fast is None: # If only one node return the head

            return slow

        while fast.next is not None:

            fast=fast.next

            slow=slow.next

        slow.next=None # Last but one node in the LinkedList, set it to None

        fast.next=head # Last node in the LinkedList set to head

        head=fast   # Now head is fast

        return head # return the new head
            



#{ 
 # Driver Code Starts
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None

def printList(node):
    while (node != None):
        print(node.data,end=" ")
        node = node.next
    print()
def inputList():
    n=int(input())#lenght of link list
    data=[int(i) for i in input().strip().split()]#all data of linked list in a line
    head = Node(data[0])
    tail = head;
    for i in range(1,n):
        tail.next = Node(data[i]);
        tail = tail.next;
    return head;

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        head = inputList()
        
        obj = Solution()
        res = obj.moveToFront(head)
        
        printList(res)
        

# } Driver Code Ends