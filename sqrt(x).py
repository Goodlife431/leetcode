class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        guess = x // 2
        while guess * guess > x:
            guess = (guess + x // guess) // 2
        return guess