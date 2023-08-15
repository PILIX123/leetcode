class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums.reverse()
        x = 0
        try:
            while x < len(nums):
                if nums[x] == nums[x + 1]:
                    nums.pop(x)
                    continue
                x += 1
        except IndexError:
            nums.reverse()