from listNode import ListNode

class Dict:
    def __init__(self):
        self.head = None
    
    def insert(self, val):
        if self.head is None:
            self.head = ListNode(val)
            self.head.next = self.head
        else:
            node = ListNode(val, self.head.next)
            self.head.next = node
    
    def search(self, val):
        if self.head is None: return None
        pointer = self.head
        while pointer.val != val:
            pointer = pointer.next
            if pointer == self.head:
                break
        else:
            return pointer
        return None
    
    def delete(self, val):
        pointer = self.head
        while pointer.next.val != val:
            pointer = pointer.next
        pointer.next = pointer.next.next
