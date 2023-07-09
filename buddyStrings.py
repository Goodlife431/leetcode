# Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

# For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

class solution(object):
    def buddy_strings(self, s , goal):
        if len(s) != len(goal):
            return False
        
        if s == goal:
            return len(set(s)) < len(s)
        
        diff_s = []
        diff_goals = []

        for i in range(len(s)):
            if s[i] != goal[i]:
                diff_s.append(s[i])
                diff_goals.append(goal[i])
                if len(diff_s) > 2:
                    return False

        return len(diff_s) == 2 and diff_s == diff_goals[::-1]
     



