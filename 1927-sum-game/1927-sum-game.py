class Solution:
    def sumGame(self, num):
        n = len(num)
        half = n // 2

        sumL = sumR = 0
        cntL = cntR = 0

        # left half
        for i in range(half):
            if num[i] == '?':
                cntL += 1
            else:
                sumL += int(num[i])

        # right half
        for i in range(half, n):
            if num[i] == '?':
                cntR += 1
            else:
                sumR += int(num[i])

        # odd '?' → Alice wins
        if (cntL + cntR) % 2 == 1:
            return True

        # check condition
        return not (sumL - sumR == (cntR - cntL) * 9 // 2)
        