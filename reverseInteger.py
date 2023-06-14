class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x = abs(x)

        reversed_x = 0
        while x > 0:
            reversed_x = (reversed_x * 10) + (x % 10)
            x = x // 10

        if reversed_x > 2**31 - 1:
            return 0

        return sign * reversed_x
