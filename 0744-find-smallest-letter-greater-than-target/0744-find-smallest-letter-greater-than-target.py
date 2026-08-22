class Solution(object):
    def nextGreatestLetter(self, letters, target):
        start = 0
        end = len(letters) - 1

        while start <= end:
            mid = (start + end) // 2

            if letters[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return letters[start % len(letters)]            