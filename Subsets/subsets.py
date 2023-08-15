class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        def solve(i, curr):
            if i >= len(nums):
                res.append(curr.copy())
                return 
            curr.append(nums[i])
            solve(i+1, curr)

            curr.pop()
            solve (i+1, curr)
        solve(0,[])
        return res