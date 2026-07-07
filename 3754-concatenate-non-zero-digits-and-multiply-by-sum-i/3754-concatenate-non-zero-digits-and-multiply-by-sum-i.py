class Solution:
    def sumAndMultiply(self, n: int) -> int:
        p = 1
        x = 0
        s = 0

        while n > 0:
            digit = n % 10
            s += digit

            if digit != 0:
                x += digit * p
                p *= 10

            n //= 10

        return x * s