# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        paths = []

        def helper(node, path,paths):
            if not node:
                return
            path += str(node.val)
            if not node.left and not node.right:
                paths.append(path)
            else:
                path += "->"
                helper(node.left, path, paths)
                helper(node.right, path, paths)

        paths = []
        helper(root, "" ,paths)
        return paths        

        