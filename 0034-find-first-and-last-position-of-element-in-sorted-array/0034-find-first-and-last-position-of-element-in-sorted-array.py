class Solution(object):
    def searchRange(self, nums, target):
        
        def findFirst(nums, target):
            start = 0
            end = len(nums) - 1
            result = -1

            while start <= end:
                mid = (start + end ) // 2
                
                if nums[mid] == target:
                    result =  mid
                    end = mid - 1
                elif nums[mid] > target:
                    end = mid -1
                else:
                    start = mid + 1
            return result

        def findLast(nums, target):
            start = 0
            end = len(nums) - 1
            result = -1

            while start <= end:
                mid = (start + end ) // 2
               
                if nums[mid] == target:
                    result =  mid
                    start = mid + 1
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return result
        return [findFirst(nums, target), findLast(nums, target)]                


        