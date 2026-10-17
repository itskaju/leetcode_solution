
from collections import deque
from typing import Optional

# LeetCode provides the Node class.

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        queue = deque([root])

        while queue:
            size = len(queue)
            prev = None

            for _ in range(size):
                node = queue.popleft()

                if prev:
                    prev.next = node

                prev = node

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            # The last node at this level points to None.
            prev.next = None

        return root

