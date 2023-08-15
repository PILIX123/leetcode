class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits.reverse()
        for index, digit in enumerate(digits):
            if digit == 9:
                digits[index] = 0
                if index + 1 == len(digits):
                    digits.append(0)
                continue
            digits[index] += 1
            break
        return reversed(digits)
