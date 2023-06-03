import unittest

def isVaild(self, s):
    map_dict = dict(('()', '{}', '[]'))
    stack = []
    for index in s:
        if index in '({[':
            stack.append(index)
        elif len(stack) == 0 or index != map_dict[stack.pop()]:
            return False
    return len(stack) == 0



class SolutionTest(unittest.TestCase):
    def test_isValid(self):
        self.assertTrue(self.solution.isValid('()'))


if __name__ == '__main__':
    unittest.main()