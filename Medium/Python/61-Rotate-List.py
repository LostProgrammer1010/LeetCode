def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

  if head is None:
    return head


  length = 1
  end = head
  while(end.next):
    end = end.next
    length += 1

  k = k % length

  end.next = head

  for _ in range(length - k - 1):
    head = head.next

  ans = head.next
  head.next = None

  return ans