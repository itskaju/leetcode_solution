class Solution:
    def sumSubarrayMins(self, arr):
        MOD = 10**9 + 7
        n = len(arr)

        prev = [-1] * n          # Previous Smaller Element
        nxt = [n] * n            # Next Smaller or Equal Element

        stack = []

        # Previous Smaller (<)
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()

            if stack:
                prev[i] = stack[-1]

            stack.append(i)

        stack = []

        # Next Smaller or Equal (<=)
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()

            if stack:
                nxt[i] = stack[-1]

            stack.append(i)

        ans = 0

        for i in range(n):
            left = i - prev[i]
            right = nxt[i] - i
            ans = (ans + arr[i] * left * right) % MOD

        return ans