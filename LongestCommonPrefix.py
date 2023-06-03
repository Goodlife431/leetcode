# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        prefix = strs[0]
        for word in strs:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
        return prefix