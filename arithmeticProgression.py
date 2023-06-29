class solution(object):
    def arithemitic_progression(arr):
        arr.sort()
        diff = arr[1] - arr[0]
        
        for i in range(2, len(arr)):
            current_diff = arr[i] - arr[i-1]
            if current_diff != diff:
                return False
        return True