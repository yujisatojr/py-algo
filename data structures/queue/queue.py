class Queue:
    def __init__(self):
        self.head = None
        self.size = 0

    def enqueue(self, d):
        newNode = Node(d)
        if (self.head == None):
            self.head = newNode
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = newNode
        self.size = self.size + 1

    def dequeue(self):
        if (self.size == 0):
            print('The queue is empty!')
        else:
            result = None
            current = self.head
            result = self.head.data
            self.head = self.head.next
            self.size = self.size - 1
            return result

    def peek(self):
        print(self.head.data)

    def clear(self):
        self.head = None
        size = 0

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

q = Queue()
q.enqueue('Pikachu')
q.enqueue('Squirtle')
q.dequeue()
q.enqueue('Charmander')
# q.clear()
q.printAll()
#q.peek()
