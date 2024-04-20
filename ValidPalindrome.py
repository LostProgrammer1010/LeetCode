def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = "".join(c for c in s if c.isalpha() or c.isalnum())
    right = len(s) - 1
    left = 0

    while rigth > left:
        if s[right] != s[left]:
            return False
        left += 1
        right -= 1
