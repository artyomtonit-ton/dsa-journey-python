nums = [1, 2, 3, 4]

def sum_array(nums):
    list_sum = [nums[0]]
    res = nums[0]
    for i in range(1, len(nums)):
        res += nums[i]
        list_sum.append(res)

    return list_sum

print(sum_array(nums))