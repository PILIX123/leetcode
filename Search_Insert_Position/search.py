class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        try:
            for index in range(len(nums)):
                if nums[index] >= target:
                    return index
                elif nums[index + 1] > target:
                    return index + 1
        except IndexError:
            return index + 1
