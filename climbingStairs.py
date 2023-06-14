# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

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