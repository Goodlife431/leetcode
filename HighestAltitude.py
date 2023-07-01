class solution(object):
    def highest_altitude(self, gain):
        highest = 0
        altitude = 0
        for g in gain:
            altitude += g
            highest = max(highest, altitude)
        return highest