def two_sum(nums, target):
    temp_dict = dict()
    for i in range(len(nums)):
        if (target - nums[i]) in temp_dict:
            return [temp_dict[target - nums[i]], i]
        if nums[i] not in temp_dict:
            temp_dict[nums[i]] = i
            print(temp_dict)


numbers = [2, 2, 5, 8]
s = 7
print(two_sum(numbers, s))
