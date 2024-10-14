def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = head

        while(head):
            nxt = head.next

            while(nxt and head.val == nxt.val):
                nxt = nxt.next
            
            head.next = nxt
            head = head.next

        return start
