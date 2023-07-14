class solution(object):
    def is_palindrome(self, s):
        modified_s = ""
        for char in s:
            if char.isalnum():
                modified_s += char.lower()

        reversed_s = modified_s[::-1]
        return modified_s == reversed_s
    