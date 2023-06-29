class solution(object):
    def getMinimumDifference(self, root):
        stack = []
        current = root
        prev_val = None
        min_diff = float('inf')

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            if prev_val is not None:
                min_diff = min(min_diff, current.val - prev_val)
            prev_val = current.val

            current = current.right
        return min_diff
