
class Solution:
    def flatten(self, root):
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        left = root.left
        right = root.right

        root.left = None
        root.right = left

        curr = root

        while curr.right:
            curr = curr.right

        curr.right = right

