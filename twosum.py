from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict={}
        for index, val in enumerate(nums):
            if target - val in dict:
                return dict[target-val], index
            dict[val] = index
    def isPalindrome(self, x: int) -> bool:
        pal = ""
        val = x
        if(x<0):
            return False
        if(x==0):
            return True
        while val > 0:
            pal+=str(val%10)
            val = int(val/10)
        if(int(pal)==x):
            return True
        return False
    def romanToInt(self, s: str) -> int:
        dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000}
        value = 0
        prev = ''
        roman = s[::-1]
        for char in roman:
            if prev in dict:
                if dict[prev] > dict[char]:
                    value-=dict[char]
                else:
                    value+=dict[char]
            else:
                value+=dict[char]
            prev = char
        return value
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
    def isValid(self, s: str) -> bool:
        dict={
            "{": 0,
            "[": 0,
            "(": 0 
        }
        dictreverse = {
            "}":"{",
            "]":"[",
            ")":"("
        }
        last=[]
        for char in s:
            if char in dict:
                dict[char]+=1
                last.append(char)
            else:
                if dict[dictreverse[char]] !=0 and last[len(last)-1] == dictreverse[char]:
                    dict[dictreverse[char]]-=1
                    last.pop()
                else:
                    return False
        for val in dict.values():
            if val > 0:
                return False
        return True
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return