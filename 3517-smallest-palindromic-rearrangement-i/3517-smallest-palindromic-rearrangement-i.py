class Solution:
    def smallestPalindrome(self,  s:str) -> str:
        cnt = Counter(s)
        first_half = []
        middle = ""

        for ch in sorted(cnt.keys()):
            first_half.append(ch * (cnt[ch] //2))
            if cnt[ch] % 2 == 1:
                middle = ch

        first_half_str = "" . join(first_half)
        return first_half_str + middle + first_half_str[:: - 1]        