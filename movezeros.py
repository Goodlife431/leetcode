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