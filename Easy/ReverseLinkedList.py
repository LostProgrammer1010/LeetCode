def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = listNode()
    newhead = ListNode()

    if head is None:
        return head

    if head.next is None:
        return head

    if head.next.next is None:
        temp = head.next
        head.next.next = head
        head.next = None
        return temp

    previous = None
    current = head

    while(head):
        tempNode = head.next.next
        head.next.next = head
        tempprev = head.next
        head.next = previous
        prevous = tempprev
        head = tempNode

    head.next = previous

    return head
