class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addNode(self, d):
        nd = Node(d)
        if (self.head == None):
            self.head = nd
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = nd
        size = self.size + 1

    def size():
        return size

    def printAll(self):
        current = self.head
        while (current != None):
            print(current.data)
            current = current.next

class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

lnl = LinkedList()
lnl.addNode('Yuji')
lnl.addNode('Yuji')
lnl.addNode('Yuji')
lnl.printAll()
