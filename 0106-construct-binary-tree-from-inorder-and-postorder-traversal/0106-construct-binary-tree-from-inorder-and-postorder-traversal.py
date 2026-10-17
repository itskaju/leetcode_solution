from typing import List, Optional

# LeetCode provides the TreeNode class automatically.
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index_map = {value: i for i, value in enumerate(inorder)}
        post_idx = len(postorder) - 1

        def build(left: int, right: int) -> Optional[TreeNode]:
            nonlocal post_idx

            if left > right:
                return None

            # The last remaining postorder element is the root.
            root_val = postorder[post_idx]
            post_idx -= 1

            root = TreeNode(root_val)
            mid = index_map[root_val]

            # Build right subtree first, then left subtree.
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)