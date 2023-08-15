class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        shortest = 0
        prev = 1000
        for short, word in enumerate(strs):
            if(prev > len(word)):
                prev = len(word)
                shortest = short
        for index, char in enumerate(strs[shortest]):
            count = 0
            for word in strs:
                if word[index] == char:
                    count+=1
            if count == len(strs):
                prefix+=char
            else:
                return prefix
        return prefix