class Solution:
    def firstUniqChar(self, s: str) -> int: 

        freq = {}

        # count the number of frquency
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

            # count the unique ch
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i

        return -1                              

