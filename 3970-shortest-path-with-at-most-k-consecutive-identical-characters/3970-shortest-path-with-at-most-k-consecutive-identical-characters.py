from typing import List
import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))

        # State is (node, current consecutive-label run length).
        dist = [[float("inf")] * (k + 1) for _ in range(n)]
        start_run = 1
        if start_run > k:
            return -1

        dist[0][start_run] = 0
        pq = [(0, 0, start_run)]

        while pq:
            cost, u, run = heapq.heappop(pq)
            if cost != dist[u][run]:
                continue
            if u == n - 1:
                return cost

            for v, weight in graph[u]:
                next_run = run + 1 if labels[u] == labels[v] else 1
                if next_run > k:
                    continue

                next_cost = cost + weight
                if next_cost < dist[v][next_run]:
                    dist[v][next_run] = next_cost
                    heapq.heappush(pq, (next_cost, v, next_run))

        return -1