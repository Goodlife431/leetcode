class Solution(object):
    def signfunction(self, x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0
        
    def arraySign(self, nums):
        product = 1
        for num in nums:
            product *= num
        return self.signfunction(product)