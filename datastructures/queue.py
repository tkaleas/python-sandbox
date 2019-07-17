class Queue:
    def __init__(self, head=None):
        self.storage = [head]

    def enqueue(self, new_element):
        self.storage.insert(0,new_element)

    def peek(self):
        return self.storage[-1]

    def dequeue(self):
        return self.storage.pop(len(self.storage)-1)