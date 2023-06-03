class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        char_map = {}
        max_length = 0
        start = 0
        for end in range(n):
            if s[end] in char_map:
                start = max(start, char_map[s[end]] + 1)
            
            char_map[s[end]] = end
            max_length = max(max_length, end - start + 1)

        return max_length
        