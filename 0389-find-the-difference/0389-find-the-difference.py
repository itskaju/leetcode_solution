class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        for ch in s + t:   # combine both strings
            result ^= ord(ch)   # XOR ASCII value of character
        return chr(result)      # convert back to character
