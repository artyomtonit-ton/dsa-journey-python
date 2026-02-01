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
"""

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sums = [nums[0]]
        current_sum = nums[0]
        
        for i in range(1, len(nums)):
            current_sum += nums[i]
            running_sums.append(current_sum)

        return running_sums

if __name__ == "__main__":
    sol = Solution()
    print(sol.runningSum([1, 2, 3, 4]))