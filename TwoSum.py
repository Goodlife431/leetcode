class solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i,j] 
                
    def test_find_sum_pair():
        nums = [2, 7, 11, 15]
        target = 9
        expected_output = [0, 1]  

        
        actual_output = find_sum_pair(nums, target)

        
        assert actual_output == expected_output, f"Expected {expected_output}, but got {actual_output}"

        
        nums = [3, 1, 4, 6]
        target = 10
        expected_output = [2, 3]  

        actual_output = find_sum_pair(nums, target)
        assert actual_output == expected_output, f"Expected {expected_output}, but got {actual_output}"

        print("All test cases passed!")


    test_find_sum_pair()
