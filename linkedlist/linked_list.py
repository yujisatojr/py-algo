class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addNode(self, d):
        nd = Node()
        nody = nd.node(d)
        if (self.head == None):
            head = nody
        else:
            current = head
            while (current.next != None):
                current = current.next
            current.next = node
        size = self.size + 1

    def size():
        return size

    def printAll(self):
        current = self.head
        while (current != None):
            print(current.data)
            current = current.next

class Node:

    def node(self, d):
        self.data = d
        next = None

lnl = LinkedList()
data = 'Yuji'
lnl.addNode(data)
lnl.printAll()
