class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        freq = {}

        # count every ch in magazine
        for ch in magazine:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1   

        for ch in ransomNote:
            if ch not in freq:
                return False

            freq[ch] -= 1

            if freq[ch] < 0:
                return False


        return True

        