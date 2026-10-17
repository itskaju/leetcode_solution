
class Solution:
    def maxPathSum(self, root):
        self.maximum = float('-inf')

        def dfs(node):
            if not node:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            self.maximum = max(
                self.maximum,
                node.val + left + right
            )

            return node.val + max(left, right)

        dfs(root)
        return self.maximum

    