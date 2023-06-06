class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ''
    
        def expandFromCenter(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
    
        for i in range(len(s)):
            palindrome_odd = expandFromCenter(s, i, i)
            palindrome_even = expandFromCenter(s, i, i+1)
            
            longest = max(longest, palindrome_odd, palindrome_even, key=len)
        
        return longest
        