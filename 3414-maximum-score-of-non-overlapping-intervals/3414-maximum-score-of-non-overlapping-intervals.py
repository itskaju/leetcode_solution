from bisect import bisect_left
from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)
        
        arr = [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
        arr.sort(key=lambda x: x[1])
        
        ends = [x[1] for x in arr]
        
        prev = []
        for i in range(n):
            l = arr[i][0]
            j = bisect_left(ends, l) - 1
            prev.append(j)
        
        dp = [[(0, []) for _ in range(n)] for _ in range(5)]
        
        for i in range(n):
            l, r, w, idx = arr[i]
            
            for k in range(1, 5):
                # skip
                best = dp[k][i-1] if i > 0 else (0, [])
                
                # take
                j = prev[i]
                if j >= 0:
                    prev_weight, prev_list = dp[k-1][j]
                else:
                    prev_weight, prev_list = (0, [])
                
                candidate = (prev_weight + w, prev_list + [idx])
                
                if (candidate[0] > best[0] or 
                   (candidate[0] == best[0] and sorted(candidate[1]) < sorted(best[1]))):
                    dp[k][i] = candidate
                else:
                    dp[k][i] = best
        
        res = (0, [])
        for k in range(1, 5):
            cur = dp[k][n-1]
            if (cur[0] > res[0] or 
               (cur[0] == res[0] and sorted(cur[1]) < sorted(res[1]))):
                res = cur
        
        return sorted(res[1])