
from .linkedlist import LinkedList

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def peek(self):
        "Peek at the top of the stack but do not pop off"
        return self.ll.head
        
    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)
        pass

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()