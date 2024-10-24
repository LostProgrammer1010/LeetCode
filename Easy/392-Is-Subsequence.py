def isSubsequence(self, s: str, t: str) -> bool:
        index = 0

        if not s:
            return True

        for letter in t:
            if letter == s[index]:
                index += 1
            if index == len(s):
                return True
