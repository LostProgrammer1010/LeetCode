class Solution:
  def canAliceWin(self, n: int) -> bool:
    alice_turn = True
    stone_taken = 10
    while(n - stone_taken >= 0):
      alice_turn = not alice_turn
      n -= stone_taken
      stone_taken -= 1
      
    return not alice_turn