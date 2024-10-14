def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        end = len(needle)

        while(end < len(haystack)+1):
            if haystack[i:end] == needle:
                return i
            i += 1
            end += 1

        return -1
