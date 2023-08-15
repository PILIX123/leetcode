class Solution:
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