# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



from itertools import permutations

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(permutations(nums))