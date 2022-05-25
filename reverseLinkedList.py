from listNode import ListNode, makeLinkedList

def reverseLinkedList(head):
    if not head or not head.next: return head
    curr = head.next
    prev = head
    head.next = None
    while curr.next:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    else:
        curr.next = prev
    return curr

if __name__ == '__main__':
    ll = makeLinkedList([1, 2, 3, 4])
    print(reverseLinkedList(ll))
