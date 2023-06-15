class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31

        if divisor == 0:
            return MAX_INT if dividend > 0 else MIN_INT
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        negative = (dividend < 0) != (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        while dividend >= divisor:
            temp_divisor = divisor
            multiple = 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            dividend -= temp_divisor
            quotient += multiple
        return -quotient if negative else quotient 
