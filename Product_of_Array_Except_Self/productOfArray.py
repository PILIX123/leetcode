import math
class Solution:
    """
    first solution with big time complexity
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = []

        for i in range(nums):
            temp = nums.copy()
            temp.pop(i)
            res.append(math.prod(temp))


        return res"""
    #From neetcode with O(n) complexity
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
