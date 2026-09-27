class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n = len(nums)
        threshold = n // 3
        count_map = {}
        result = []

        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

        for num, count in count_map.items():
            if count > threshold:
                result.append(num)

        return result
