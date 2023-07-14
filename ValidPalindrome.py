# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

class solution(object):
    def is_palindrome(self, s):
        modified_s = ""
        for char in s:
            if char.isalnum():
                modified_s += char.lower()

        reversed_s = modified_s[::-1]
        return modified_s == reversed_s
    