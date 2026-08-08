class Solution:
    def validSequence(self, word1: str, word2: str):
        n, m = len(word1), len(word2)

        # Step 1: Build last array
        last = [-1] * m
        j = m - 1

        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                last[j] = i
                j -= 1

        # Step 2: Greedy build answer
        ans = []
        skip = 0  # mismatch used or not
        j = 0

        for i in range(n):
            if j == m:
                break

            # condition to take index
            if (word1[i] == word2[j] or
               (skip == 0 and (j == m - 1 or i < last[j + 1]))):

                if word1[i] != word2[j]:
                    skip = 1

                ans.append(i)
                j += 1

        return ans if j == m else []