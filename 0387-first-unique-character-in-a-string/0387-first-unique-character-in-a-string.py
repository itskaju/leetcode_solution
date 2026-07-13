class Solution:
    def firstUniqChar(self, s: str) -> int:

        freq = {}

        # count frequency 
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1 

        # find first unique frequency ch
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i

        return -1                 
