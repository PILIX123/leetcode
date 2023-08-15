class Solution:
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
