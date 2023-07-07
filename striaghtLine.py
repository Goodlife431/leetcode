class solution(object):
    def checkStraightLine(coordinates):
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        
        slope = (y1 - y0) / (x1 -x0)

        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if(y -y0) / (x - x0) != slope:
                return False
            
        return True
