# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

class solution(object):
    def myPow(self, x, n):
        result = 1

        if n < 0:
            x = 1 / x
            n = -n
        
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2

        return result