"""
1480. Running Sum of 1d Array
Difficulty: Easy
Topic: Arrays, Prefix Sum

Description:
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Описание:
Дан массив nums. Верни массив "текущих сумм".
Элемент result[i] должен быть равен сумме всех чисел от начала массива до индекса i включительно.

Example:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: [1, 1+2, 1+2+3, 1+2+3+4].
"""

nums = [1, 2, 3, 4]

def sum_array(nums):
    list_sum = [nums[0]]
    res = nums[0]
    for i in range(1, len(nums)):
        res += nums[i]
        list_sum.append(res)

    return list_sum

print(sum_array(nums))