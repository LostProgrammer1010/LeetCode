def removeDuplicates(self, nums: List[int]) -> int:
  ans = head

  while(head and head.next):
    if head.val == head.next.val:
      temp = head
      while(temp and temp.val == head.val):
        temp = temp.next
      head.next = temp
    head = head.next


  return ans

