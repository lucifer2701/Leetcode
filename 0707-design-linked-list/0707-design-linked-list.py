class Node:
		def __init__(self, val):
			self.val = val
			self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if index < 0 or index > 1000 or not self.head: 
            return -1

        i = 0
        currentNode = self.head
        while currentNode.next and i != index :
            i += 1
            currentNode = currentNode.next

        return currentNode.val if i==index else -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node

    def addAtTail(self, val: int) -> None:
        if self.head : 
            currentNode = self.head
            while currentNode.next:
                currentNode = currentNode.next

            currentNode.next = Node(val)
        else:
            self.addAtHead(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        elif self.head:
            i = 0
            prevNode = None
            currentNode = self.head
            while currentNode.next and i != index :
                i += 1
                prevNode = currentNode
                currentNode = currentNode.next

            if index == i:
                newNode = Node(val)
                prevNode.next = newNode
                newNode.next = currentNode
            elif index == i+1:
                currentNode.next = Node(val)


    def deleteAtIndex(self, index: int) -> None:
        if  self.head:
            i = 0
            prevNode = None
            currentNode = self.head
            while currentNode.next and i != index :
                i += 1
                prevNode = currentNode
                currentNode = currentNode.next

            if i == index: 
                if i == 0:
                    self.head = currentNode.next
                else :
                    prevNode.next = currentNode.next
                del currentNode