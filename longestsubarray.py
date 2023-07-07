class solution(object):
    def longestSubarray(self, nums, threshold):
        n = len(nums)
        left = 0
        maxLength = 0
        evenCount = 0

        for right in range(n):
            if nums[right] % 2 == 0:
                evenCount += 1
            
            if right - left + 1 - evenCount > threshold:
                if nums[left] % 2 == 0:
                    evenCount -= 1
                left += 1

            maxLength = max(maxLength, right - left + 1)

        return maxLength
