class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, d):
        newNode = Node(d)
        if (self.head == None):
            self.head = newNode
        else:
            current = self.head
            while (current.next != None):
                current = current.next
            current.next = newNode
        self.size = self.size + 1

    def pop(self):
        index = self.size - 1
        if (self.size == 0):
            print('The stack is empty!')
        else:
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

    def peek(self):
        index = self.size - 1
        current = self.head
        if (index == 0):
            print(self.head.data)
        else:
            for i in range(0, index - 1):
                current = current.next
            print(current.next.data)

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

stk = Stack()
stk.push('Pikachu')
stk.push('Squirtle')
stk.push('Charmander')
stk.pop()
# stk.clear()
stk.printAll()
stk.peek()
