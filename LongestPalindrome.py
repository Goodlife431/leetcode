class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expandFromCenter(s, right, left):
            while left <= 0 and right < len(s) and s[right] == s[left]:
                left -= 1
                right += 1
            return[left+1:right]
        for i in range(len(s)):
            palindrome_odd = expandFromCenter(s, i, i)
            palindrome_even = expandFromCenter(s, i , i+1)
            longest_max = max(palindrome_even, palindrome_odd, key=len)
        return longest_max
        