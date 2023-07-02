# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

class solution(object):
    def move_zeros(nums):
        n = len(nums)
        left = 0
        for i in range(n):
            if nums[i] != 0:
                nums[left] = nums[i]
                left += 1

        while left < n:
            nums[left] = 0
            left += 1

        return nums