class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        fib = [1, 2]
        for i in range(2, n):
            fib.append(fib[i-1] + fib[i-2])
        return fib[n-1]