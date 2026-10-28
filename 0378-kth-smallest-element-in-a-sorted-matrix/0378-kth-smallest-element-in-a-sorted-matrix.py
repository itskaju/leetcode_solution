class Solution(object):
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        min_heap = []

        for row in range(min(n,k)):
            heapq.heappush(min_heap, (matrix[row][0], row,0))

        for _ in range(k-1):
            value, row, col = heapq.heappop(min_heap)

            if col+ 1 < n:
                heapq.heappush(
                    min_heap,
                    (matrix[row][col+1], row, col+1)
                )  
        return heapq.heappop(min_heap)[0]                 