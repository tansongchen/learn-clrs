from listNode import ListNode

class Queue:
    def __init__(self):
        self.list = None
        self.tail = None
    
    def enqueue(self, val):
        if self.tail is None:
            self.list = self.tail = ListNode(val)
        else:
            self.tail.next = ListNode(val)
    
    def dequeue(self):
        val = self.list.val
        self.list = self.list.next
        return val