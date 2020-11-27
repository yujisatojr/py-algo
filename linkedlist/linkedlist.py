from node import Node

class LinkedList:
    #def __init__(self):
    #    self.head = null
    #    self.size = 0

    def addNode(d):
        head = null
        size = 0
        node = Node(d)
        if (head == null):
            head = node
        else:
            current = head
            while (current.next != null):
                current = current.next
            current.next = node
        size = size + 1

    def size():
        return size

    def printAll():
        current = head
        while (current != null):
            print(current.data)
            current = current.next
