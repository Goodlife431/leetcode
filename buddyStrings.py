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
     



