"""
1365. How Many Numbers Are Smaller Than the Current Number
Difficulty: Easy
Topic: Arrays, Nested Loops

Description:
Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it.
That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Описание:
Дан массив nums. Для каждого элемента нужно посчитать, сколько чисел в этом же массиве меньше него.
Нужно вернуть массив с этими количествами.

Example:
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
"""

from typing import List

class Solution:
    def findSmallerNumber(self, nums: List[int]) -> List[int]:
        smaller_nums = []
        
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    count += 1
            smaller_nums.append(count)
                    
        return smaller_nums

if __name__ == "__main__":
    s = Solution()
    print(s.findSmallerNumber([8, 1, 2, 2, 3]))