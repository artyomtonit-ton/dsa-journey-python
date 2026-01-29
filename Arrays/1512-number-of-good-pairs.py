nums = [1, 2, 3, 1, 1, 3]

def find_goodpairs(nums):
    count = 0

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j] and i < j:
                count += 1
    
    return count

print(find_goodpairs(nums))