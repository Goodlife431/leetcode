# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

class solution(object):
    def can_palace_flowers(self, flowerbed, n):
        flowerbed = [0] + flowerbed + [0]
        count = 0
        i = 1

        while i < len(flowerbed) - 1:
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                count += 1
                i += 2
            else:
                i += 1
        return count >= n
        

