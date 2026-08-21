import math
from itertools import combinations

class Solution(object):
    def findKthSmallest(self, coins, k):
        
        # 🔹 Step 1: remove redundant coins
        coins = sorted(set(coins))
        filtered = []
        for c in coins:
            if all(c % x != 0 for x in filtered):
                filtered.append(c)
        coins = filtered
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        def lcm(a, b):
            return a * b // gcd(a, b)
        
        def count(x):
            total = 0
            n = len(coins)
            
            for i in range(1, n + 1):
                for comb in combinations(coins, i):
                    curr_lcm = comb[0]
                    for num in comb:
                        curr_lcm = lcm(curr_lcm, num)
                    
                    if i % 2 == 1:
                        total += x // curr_lcm
                    else:
                        total -= x // curr_lcm
            return total
        
        low, high = 1, 10**18
        
        while low < high:
            mid = (low + high) // 2
            
            if count(mid) >= k:
                high = mid
            else:
                low = mid + 1
        
        return low