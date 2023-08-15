class Solution:
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