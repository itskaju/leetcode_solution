class Solution(object):
    def maxSlidingWindow(self, nums, k):

       tree = SortedList()
       ans = []
       
       for i in range(len(nums)):
            tree.add(nums[i])

            if i >=k:
                tree.remove(nums[i-k])

            if i >= k-1:
                ans.append(tree[-1])

       return ans        
        