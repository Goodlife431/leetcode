# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

class solution(object):
    def canJump(self, nums):
        max_reachable = 0
        n = len(nums)
        for i in range(n):
            if i > max_reachable:
                return False
            max_reachable = max(max_reachable, i + nums[i])

        return max_reachable >= n - 1 