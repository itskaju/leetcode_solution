from typing import List

class Solution:
    def countServers(
        self, n: int, logs: List[List[int]], x: int, queries: List[int]
    ) -> List[int]:
        logs.sort(key=lambda log: log[1])
        indexed_queries = sorted(
            (query, i) for i, query in enumerate(queries)
        )

        counts = {}
        left = right = 0
        result = [0] * len(queries)

        for query, original_index in indexed_queries:
            # Include logs in the interval [query - x, query].
            while right < len(logs) and logs[right][1] <= query:
                server = logs[right][0]
                counts[server] = counts.get(server, 0) + 1
                right += 1

            while left < right and logs[left][1] < query - x:
                server = logs[left][0]
                counts[server] -= 1
                if counts[server] == 0:
                    del counts[server]
                left += 1

            result[original_index] = n - len(counts)

        return result