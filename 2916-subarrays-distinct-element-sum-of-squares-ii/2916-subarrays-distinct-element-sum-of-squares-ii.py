from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        size = 4 * n
        total = [0] * size
        squares = [0] * size
        lazy = [0] * size

        def apply(node, left, right, val):
            length = right - left + 1
            squares[node] = (
                squares[node] + 2 * val * total[node] + length * val * val
            ) % MOD
            total[node] = (total[node] + length * val) % MOD
            lazy[node] = (lazy[node] + val) % MOD

        def push(node, left, right):
            if lazy[node] == 0 or left == right:
                return

            mid = (left + right) // 2
            val = lazy[node]

            apply(node * 2, left, mid, val)
            apply(node * 2 + 1, mid + 1, right, val)

            lazy[node] = 0

        def update(node, left, right, ql, qr, val):
            if ql > right or qr < left:
                return

            if ql <= left and right <= qr:
                apply(node, left, right, val)
                return

            push(node, left, right)
            mid = (left + right) // 2

            update(node * 2, left, mid, ql, qr, val)
            update(node * 2 + 1, mid + 1, right, ql, qr, val)

            total[node] = (total[node * 2] + total[node * 2 + 1]) % MOD
            squares[node] = (
                squares[node * 2] + squares[node * 2 + 1]
            ) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            prev = last.get(x, -1)

            update(1, 0, n - 1, prev + 1, i, 1)

            ans = (ans + squares[1]) % MOD
            last[x] = i

        return ans