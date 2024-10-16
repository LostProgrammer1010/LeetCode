def lengthOfLongestSubstring(s: str) -> int:
    if not s:
        return 0

    longest = s[0]

    for i in range(len(s)):
        test = s[i]
        for x in range(i+1, len(s)):
            if s[x] in test:
                test = ""
                break
            test += s[x]
            if len(test) > len(longest):
                longest = test
        return longests
