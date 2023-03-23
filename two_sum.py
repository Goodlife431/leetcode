def two_sum(nums, target):
    hash_map = {}
    for i in range(len(nums)):
        if target - nums[i] in hash_map:
            return [hash_map[target - nums[i]], i]
        hash_map[nums[i]] = i
    else:
        return []


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    tg = 9
    two_sum(numbers, tg)
