from collections import Counter

class Solution:
    def findEvenNumbers(self, digits):
        cnt = Counter(digits)
        ans = []
        for x in range(100, 1000, 2):  # only even numbers
            cnt1 = Counter(int(d) for d in str(x))  # convert to int digits
            if all(cnt[d] >= cnt1[d] for d in cnt1):
                ans.append(x)
        return sorted(ans)  # ensure ascending order

     
        