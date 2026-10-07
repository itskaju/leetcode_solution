class Solution:
    def removeInvalidParentheses(self, s: str):
        # Step 1: Find minimum number of removals
        left_remove = 0
        right_remove = 0

        for ch in s:
            if ch == '(':
                left_remove += 1

            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        result = set()

        # Step 2: Backtracking
        def backtrack(index, left_rem, right_rem, balance, path):

            # Invalid prefix
            if balance < 0:
                return

            # No more characters
            if index == len(s):
                if left_rem == 0 and right_rem == 0 and balance == 0:
                    result.add("".join(path))
                return

            ch = s[index]

            # Option 1: Remove current parenthesis
            if ch == '(' and left_rem > 0:
                backtrack(
                    index + 1,
                    left_rem - 1,
                    right_rem,
                    balance,
                    path
                )

            if ch == ')' and right_rem > 0:
                backtrack(
                    index + 1,
                    left_rem,
                    right_rem - 1,
                    balance,
                    path
                )

            # Option 2: Keep current character
            path.append(ch)

            if ch == '(':
                backtrack(
                    index + 1,
                    left_rem,
                    right_rem,
                    balance + 1,
                    path
                )

            elif ch == ')':
                backtrack(
                    index + 1,
                    left_rem,
                    right_rem,
                    balance - 1,
                    path
                )

            else:
                backtrack(
                    index + 1,
                    left_rem,
                    right_rem,
                    balance,
                    path
                )

            path.pop()

        backtrack(0, left_remove, right_remove, 0, [])

        return list(result)