from itertools import permutations

class Solution:
    def findEvenNumbers(self, digits):
        res = set()
        
        # generate all permutations of length 3
        for perm in permutations(digits, 3):
            num = perm[0]*100 + perm[1]*10 + perm[2]
            
            # conditions: no leading zero, last digit even
            if perm[0] != 0 and perm[2] % 2 == 0:
                res.add(num)
        
        return sorted(res)

     
        