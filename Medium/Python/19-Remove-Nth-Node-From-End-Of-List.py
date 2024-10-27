def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

  # have a variable start at the beginingi of linked list
  # have a variable that start n from start
  # When n hits the end of linked list start will be n from the end

  nth_node = head

  while(n > 0):
    if not nth_node:
      nth_node = head
    else:
      nth_node = nth_node.next
      n -= 1

  del_node = head
  prev_node = head

  if not nth_node:
    nth_node = head

  while(nth_node):
    nth_node = nth_node.next
    prev_node = del_node
    del_node = del_node.next

  if del_node is None:
    head = head.next
  elif del_node != prev_node:
    prev_node.next = del_node.next
  else:
    head = None

  return head
