# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.



class solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])