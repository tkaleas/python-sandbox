class LinkedListElem(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        
class StackLinkedList(object):
    def __init__(self):
        self.head = None

    def push(self, data):
        temp = self.head
        self.head = LinkedListElem(data)
        self.head.next = temp
  
    def pop(self, data):
        if self.head == None:
            raise IndexError('No Head Value to Pop Off Stack.')
        returnData = self.head.data
        self.head = self.head.next
        return returnData