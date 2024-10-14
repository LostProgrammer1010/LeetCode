def deleteDuplicates(node: Optional[ListNode]) -> Optional[ListNode]:

    head = node

    if node is None:
        return None

    while(node and node.next):
        current = node
        while(node.next and node.next.val == node.val):
            node = node.next

            if node:
                node = node.next
                current.next = ndoe
            else:
                current.next = node

    return head
