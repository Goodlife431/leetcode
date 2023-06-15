class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        def build_bad_char_table(needle):
            bad_char_table = {}
            for i in range(len(needle) - 1):
                bad_char_table[needle[i]] = i
            return bad_char_table

        def find_first_occurrence(haystack, needle):
            m, n = len(needle), len(haystack)
            if m == 0:
                return 0
            if m > n:
                return -1

            bad_char_table = build_bad_char_table(needle)
            shift = 0
            while shift <= n - m:
                j = m - 1
                while j >= 0 and needle[j] == haystack[shift + j]:
                    j -= 1
                if j == -1:
                    return shift
                shift += max(1, j - bad_char_table.get(haystack[shift + j], -1))
            return -1

        return find_first_occurrence(haystack, needle)
