class LinkedListElement(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        """Append an Item to the End of the Linked List"""
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        cur_pos = 1
        if position < 1:
            return None
        while current:
            if position == cur_pos:
                return current
            current = current.next
            cur_pos += 1
        return None


    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head
        prev = None
        cur_pos = 1
        
        if position < 1:
            return None
            
        while current:
            if position == cur_pos:
                if prev == None:
                    new_element.next = current
                    self.head = new_element 
                else:
                    new_element.next = current
                    prev.next = new_element
                    
                return

            prev = current
            current = current.next
            
            cur_pos+=1

        return None
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        prev = current
        if self.head:
            while current.value != value:
                prev = current
                current = current.next
                if current == None:
                    return
            if current == self.head:
                self.head = current.next
                return
            prev.next = current.next

# Stack Helper Functions 
# TODO Create Unit Tests

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        new_element.next = self.head
        self.head = new_element

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        temp = self.head
        if self.head:
            self.head = self.head.next 
        return temp