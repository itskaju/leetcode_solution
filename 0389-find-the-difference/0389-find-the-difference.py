class Solution(object):
    def findTheDifference(self, s, t):
        
        freq = {}

        for ch in s:
            freq[ch]=freq.get(ch,0) + 1


        for ch in t:

            if ch not in freq or freq[ch] == 0:
               return ch

            freq[ch]-=1       