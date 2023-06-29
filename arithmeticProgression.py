# A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

# Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.



class solution(object):
    def arithemitic_progression(arr):
        arr.sort()
        diff = arr[1] - arr[0]
        
        for i in range(2, len(arr)):
            current_diff = arr[i] - arr[i-1]
            if current_diff != diff:
                return False
        return True