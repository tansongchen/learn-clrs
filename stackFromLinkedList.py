from listNode import ListNode

class Stack:
    def __init__(self):
        self.list = None
    
    def push(self, val):
        node = ListNode(val, self.list)
        self.list = node
    
    def pop(self):
        val = self.list.val
        self.list = self.list.next
        return val
    
    def top(self):
        return self.list.val
