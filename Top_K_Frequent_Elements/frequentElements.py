class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        numberDict= dict()
        for num in nums:
            val = 0 if numberDict.get(num) == None else numberDict.get(num)
            numberDict.update({num:val+1})        
        res = [x[0] for x in sorted(list(numberDict.items()),key=lambda x:x[1],reverse=True)]
        return res[:k]