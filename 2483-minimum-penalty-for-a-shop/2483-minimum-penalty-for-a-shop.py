class Solution:
    def bestClosingTime(self, customers: str) -> int:
        ans = 0
        min_penalty = customers.count('Y')
        penalty = min_penalty

        for hour in range (1,len(customers)+1):
            if customers[hour-1] == 'N' :
                penalty +=1
            else:
                penalty -= 1
            if min_penalty > penalty:
                min_penalty = penalty
                ans = hour
        return ans        


                                