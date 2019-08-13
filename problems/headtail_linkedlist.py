class LinkedListElem(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class HeadTailLinkedList(object):
    def __init__(self, data):
        self.head = LinkedListElem(data)
        self.tail = self.tail

    def delete(self, elem):
        temp = self.head
        tempPrev = None

        #Delete Head Element
        if elem == self.head:
            if self.head == self.tail:
                self.tail = None
            self.head = self.head.next
            return

        # Find Element and Previous
        while(temp != None and temp != elem):
            tempPrev = temp
            temp = temp.next

        if temp == None:
            return False # element not found

        if temp == self.tail:
            self.tail = tempPrev

        #Found Element In Temp
        # tempPrev -> temp-> temp.next
        tempPrev.next = temp.next

    def insertAfter(self, elem):
        pass 