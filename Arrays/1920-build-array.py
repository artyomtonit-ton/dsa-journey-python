nums = [0, 2, 1, 5, 3, 4]

def new_nums(nums):
    ans = [0] * len(nums) 

    for i in range(len(nums)):
        ans[i] = nums[nums[i]]

    return ans

print(new_nums(nums))