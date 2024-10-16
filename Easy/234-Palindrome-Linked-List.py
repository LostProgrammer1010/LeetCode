def isPalindrome(self, head: Optional[ListNode]) -> bool:
        pal = ""

        while(head):
            pal += str(head.val)
            head = head.next

        return pal == pal[::-1]
