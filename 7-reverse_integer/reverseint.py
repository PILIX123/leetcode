class Solution:
    def reverse(x: int) -> int:
        val = "".join(list(reversed(str(abs(x)))))
        if(int(val)>pow(2,31)-1):
            return 0
        if(x<0):
            return int(f"-{val}")
        return int(val)