class Solution:
    def reverse(self, x: int) -> int:

        reversed_num = 0
        negative = False
        if x < 0:
            negative = True
            x = abs(x)
        
        while x > 0:
            last_digit = x % 10
            reversed_num = (reversed_num * 10) + last_digit
            x = x // 10

        if negative:
            reversed_num = -reversed_num
        return reversed_num if -2**31 <= reversed_num <= 2**31-1 else 0
