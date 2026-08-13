class Solution:
    def maxPathSum(self, root):
        self.ans = float('-inf')

        def dfs(node):
            if node is None:
                return 0

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            # Complete path through current node
            self.ans = max(self.ans, node.val + left + right)

            # Return only one branch to parent
            return node.val + max(left, right)

        dfs(root)
        return self.ans