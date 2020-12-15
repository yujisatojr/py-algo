class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addNode(self, d):
        newNode = Node(d)
        if (self.head == None):
            self.head = newNode
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = newNode
        self.size = self.size + 1

    def removeAt(self, index):
        result = None
        current = self.head
        if (index == 0):
            result = self.head.data
            self.head = self.head.next
        else:
            for i in range(0, index - 1):
                current = current.next
            result = current.next.data
            current.next = current.next.next
        self.size = self.size - 1
        return result

    def insertAt(self, index, d):
        newNode = Node(d)
        current = self.head
        self.size = self.size + 1
        if (index == 0):
            newNode.next = self.head
            self.head = newNode
        else:
            for i in range(0, index - 1):
                current = current.next
            newNode.next = current.next
            current.next = newNode

    def getNode(self, index):
        current = self.head
        for i in range(0, index):
            current = current.next
        return current.data

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
lnl.addNode('Pikachu')
lnl.addNode('Squirtle')
lnl.addNode('Charmander')
lnl.insertAt(1, 'Bulbasaur')
lnl.printAll()
