class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        s = str(self.val)
        pointer = self.next
        while pointer:
            s += f' -> {pointer.val}'
            pointer = pointer.next
        return s

def makeLinkedList(a):
    if a == []: return None
    head = ListNode(a[0])
    pointer = head
    for i in range(1, len(a)):
        pointer.next = ListNode(a[i])
        pointer = pointer.next
    return head
