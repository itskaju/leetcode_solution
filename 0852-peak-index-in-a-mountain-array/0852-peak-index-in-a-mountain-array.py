class Solution(object):
    def peakIndexInMountainArray(self, arr):
        start = 0
        end = len(arr) - 1

        while start < end :
            mid = (start + end) // 2

            if arr[mid] < arr[mid + 1]:
                start = mid + 1
            else:
                end = mid 
        return start            
        