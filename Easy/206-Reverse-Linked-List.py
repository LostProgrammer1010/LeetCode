def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        array = []

        if not head:
            return head

        while(head):
            array.append(head.val)
            head = head.next
        new_head = ListNode(array[-1])
        temp = new_head

        for i in range(len(array)-2, -1, -1):
            temp.next = ListNode(array[i])
            temp = temp.next

        return new_head
