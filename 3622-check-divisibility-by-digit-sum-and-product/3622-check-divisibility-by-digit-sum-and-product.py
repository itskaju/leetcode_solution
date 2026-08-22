class Solution(object):
    def checkDivisibility(self, n):
        s = 0
        p = 1
        x = n

        while x > 0:
            digit = x % 10
            s += digit
            p *= digit
            x //= 10
        return n % (s + p) == 0    

        