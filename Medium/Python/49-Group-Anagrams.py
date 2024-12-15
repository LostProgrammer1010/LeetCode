class Solution:
    DIFF = 97
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        anagram = {}

        for string in strs:
            letter_freq = [0] * 26
            for letter in string:
                letter_freq[ord(letter.lower()) - self.DIFF] += 1
            if tuple(letter_freq) in anagram:
                anagram[tuple(letter_freq)].append(string)
            else:
                anagram[tuple(letter_freq)] = [string]
        
        return list(anagram.values())

       



        