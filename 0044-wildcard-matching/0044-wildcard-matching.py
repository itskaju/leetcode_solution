class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = 0
        j = 0

        last_star = -1
        star_match = 0

        while i < len(s):
            if j < len(p) and (p[j] == s[i] or p[j] == "?"):
                i += 1
                j += 1
            elif j < len(p)and p[j] == "*":
                last_star = j
                star_match = i
                j += 1
            elif last_star != -1:
                
                j = last_star +1
                star_match += 1
                i = star_match
            else:
                return False
        while j < len(p) and p[j] == "*":
            j += 1
        return j == len(p)                       