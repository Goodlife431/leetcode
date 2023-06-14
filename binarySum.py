class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        int_a = int(a,2)
        int_b = int(b,2)

        sum_int = int_a + int_b

        binary_sum = bin(sum_int)[2:]
        return binary_sum