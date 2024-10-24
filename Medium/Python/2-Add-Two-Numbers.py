def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
  carry = 0
  total = ListNode()
  head = total
  prev = None

  while(l1 and l2):
      addition = l1.val + l2.val + carry

      if addition > 9:
          carry = 1
          total.val = addition % 10
      else:
          carry = 0
          total.val = addition

      total.next = ListNode()
      prev = total
      total = total.next
      l1 = l1.next
      l2 = l2.next

  curr = None
  if l1:
      curr = l1
  else:
      curr = l2

  while(curr):
    addition = curr.val + carry
    if addition > 9:
        carry = 1
        total.val = addition % 10
    else:
        carry = 0
        total.val = addition
      
    total.next = ListNode()
    prev = total
    total = total.next
    curr = curr.next

  if carry == 1:
            total.val = 1

  curr = head
  if prev.next.val == 0 and prev.next.next is None:
      prev.next = None
          

  return head
