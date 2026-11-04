import heapq
from collections import defaultdict
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        
        # 1. Slide window of size x to find the min cost for every possible window
        left_heap = []   # Max-heap (stores negated values)
        right_heap = []  # Min-heap
        
        left_sum = 0
        right_sum = 0
        
        left_size = 0
        right_size = 0
        
        to_remove = defaultdict(int)
        
        def prune(heap, is_left):
            while heap:
                val = -heap[0] if is_left else heap[0]
                if to_remove[val] > 0:
                    to_remove[val] -= 1
                    heapq.heappop(heap)
                else:
                    break
        
        # cost[i] will store the min operations to equalize nums[i : i + x]
        cost = [0] * (n - x + 1)
        
        for i in range(n):
            # Add new element
            val = nums[i]
            if not left_heap or val <= -left_heap[0]:
                heapq.heappush(left_heap, -val)
                left_sum += val
                left_size += 1
            else:
                heapq.heappush(right_heap, val)
                right_sum += val
                right_size += 1
                
            # Remove old element outside window
            if i >= x:
                out_val = nums[i - x]
                to_remove[out_val] += 1
                
                # Check where it conceptually belonged to balance sums accurately
                if out_val <= -left_heap[0]:
                    left_sum -= out_val
                    left_size -= 1
                else:
                    right_sum -= out_val
                    right_size -= 1
            
            # Continuous re-balancing
            prune(left_heap, True)
            prune(right_heap, False)
            
            while left_size > right_size + 1:
                v = -heapq.heappop(left_heap)
                left_sum -= v
                left_size -= 1
                heapq.heappush(right_heap, v)
                right_sum += v
                right_size += 1
                prune(left_heap, True)
                
            while right_size > left_size:
                v = heapq.heappop(right_heap)
                right_sum -= v
                right_size -= 1
                heapq.heappush(left_heap, -v)
                left_sum += v
                left_size += 1
                prune(right_heap, False)
                
            prune(left_heap, True)
            prune(right_heap, False)
            
            # Window is fully formed
            if i >= x - 1:
                median = -left_heap[0]
                ops = (median * left_size - left_sum) + (right_sum - median * right_size)
                cost[i - x + 1] = ops

        # 2. Dynamic Programming to select k non-overlapping subarrays
        # We want to pick k non-overlapping windows of size x
        num_windows = n - x + 1
        
        # dp[j] represents the minimum operations to pick j subarrays so far
        INF = float('inf')
        dp = [INF] * (k + 1)
        dp[0] = 0
        
        # To avoid O(N * K) space, we can process window index by index using a running history
        # dp_history[i][j] keeps track of the min cost at window index `i` with `j` subarrays chosen.
        # Since we only look back `x` positions, an array or full grid works perfectly within constraints.
        grid = [[INF] * (k + 1) for _ in range(num_windows + 1)]
        grid[0][0] = 0
        
        for i in range(1, num_windows + 1):
            for j in range(k + 1):
                # Option 1: Do not choose window i-1
                grid[i][j] = grid[i-1][j]
                
                # Option 2: Choose window i-1
                if j > 0:
                    if i - x >= 0:
                        if grid[i-x][j-1] != INF:
                            grid[i][j] = min(grid[i][j], grid[i-x][j-1] + cost[i-1])
                    elif j == 1:
                        grid[i][j] = min(grid[i][j], cost[i-1])
                        
        return grid[num_windows][k]
