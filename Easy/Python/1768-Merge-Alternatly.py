def mergeAlternately(self, word1: str, word2: str) -> str:
        alternating = ""
        if len(word1) >= len(word2):
            for i in range(len(word2)):
                alternating = alternating + word1[i] + word2[i]

            if len(word1) != len(word2):
                alternating += word1[len(word2)::]

        else:
            for i in range(len(word1)):
                alternating = alternating + word1[i] + word2[i]

            alternating += word2[len(word1)::]

        return alternating
