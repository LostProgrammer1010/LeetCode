def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        for i in range(len(s)//2):
            j = -i -1
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
