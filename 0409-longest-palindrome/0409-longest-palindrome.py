class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}

        # count frequency
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        length = 0
        odd_found = False

        for val in count.values():
            if val % 2 == 0:
                length += val
            else:
                length += val - 1  # take even part
                odd_found = True

        if odd_found:
            length += 1  # one odd in center

        return length