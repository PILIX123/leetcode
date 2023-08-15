import collections
class Solution:
    """ first solution with m(n*log(n)) where n is the average lenght of the words and m is the number or words
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = dict()
        if(len(strs) == 1):
            return [strs]
        sortedStrs = list(set(["".join(sorted(st)) for st in strs]))

        for srtSt in sortedStrs:
            srtSt = "".join(srtSt)
            correct = list()
            for st in strs:
                if("".join(sorted(st)) == srtSt):
                    correct.append(st)
            res.update({srtSt:correct})
        return list(res.values())"""
    
    #Solution that reduces the time complexity to O(m*n) where n is the average lenght of the words and m is the number or words
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = dict()

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            val:list = ans.get(tuple(count))
            if(val == None):
                val = [s]
            else:
                val.append(s)
            ans.update({tuple(count):val})
        return ans.values()
