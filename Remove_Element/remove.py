class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        nums.reverse()
        x = 0
        try:
            while x < len(nums):
                if nums[x] == val:
                    nums.pop(x)
                    continue
                x += 1
        except IndexError:
            nums.reverse()