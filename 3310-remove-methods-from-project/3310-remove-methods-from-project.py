from collections import defaultdict
from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:

        graph = defaultdict(list)

        for u, v in invocations:
            graph[u].append(v)

        suspicious = [False] * n

        def dfs(node):
            suspicious[node] = True

            for nei in graph[node]:
                if not suspicious[nei]:
                    dfs(nei)

        dfs(k)

        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        ans = []

        for i in range(n):
            if not suspicious[i]:
                ans.append(i)

        return ans