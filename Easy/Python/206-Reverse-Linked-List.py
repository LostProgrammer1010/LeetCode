def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
  prev = None
  cur = head

  while(cur):
    nxt = cur.next
    cur.next = prev
    prev = cur
    if nxt is None:
      return cur
    cur = nxt

  return cur