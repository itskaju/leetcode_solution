class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        def digitProduct(x):
            product = 1

            while x:
                product *= x % 10
                x //= 10

            return product

        while True:

            if digitProduct(n) % t == 0:
                return n

            n += 1
