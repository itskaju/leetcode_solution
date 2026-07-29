from typing import List

class Solution:
    LIM = 1000005

    def C(self, n: int, k: int) -> int:
        if k > n:
            return 0
        k = min(k, n - k)
        ans = 1
        for i in range(1, k + 1):
            ans = ans * (n - i + 1) // i
            if ans > self.LIM:
                return self.LIM
        return ans

    def countWays(self, cnt: List[int]) -> int:
        total = sum(cnt)
        ans = 1
        rem = total

        for x in cnt:
            if x == 0:
                continue
            ans *= self.C(rem, x)
            if ans > self.LIM:
                return self.LIM
            rem -= x

        return ans

    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        half = [0] * 26
        mid = ""

        for i in range(26):
            half[i] = freq[i] // 2
            if freq[i] % 2:
                mid = chr(ord('a') + i)

        if self.countWays(half) < k:
            return ""

        left = []
        length = len(s) // 2

        for _ in range(length):
            for c in range(26):
                if half[c] == 0:
                    continue

                half[c] -= 1
                ways = self.countWays(half)

                if ways >= k:
                    left.append(chr(ord('a') + c))
                    break

                k -= ways
                half[c] += 1

        left = "".join(left)
        return left + mid + left[::-1]