def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:

    if head is None or head.next is None:
        return head

    if head.next.next is None:
        return head.next

    middle = head
    fast = head
    while(fast):
        if fast.next:
            fast = fast.next.next
            middle = middle.next
        else:
            break

    return middle
