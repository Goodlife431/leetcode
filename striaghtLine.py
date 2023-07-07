# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (x - x0) * (y1 - y0) != (x1 - x0) * (y - y0):
                return False

        return True