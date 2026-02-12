"""
268. Missing Number
Difficulty: Easy
Topic: Math, Bit Manipulation

Description:
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Описание:
В массиве длины n лежат числа от 0 до n. Одно число пропущено. Найди его.
(Решение через сумму — самое быстрое).

Example:
Input: nums = [3,0,1]
Output: 2
"""

from typing import List

class Solution:
    def findMissingSlow(self, nums: List[int]) -> int:
        for i in range(len(nums) + 1):
            if i not in nums:
                return i
            
    def findMissingFast(self, nums: List[int]) -> int:
        return (len(nums) * (len(nums) + 1) // 2) - sum(nums)
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.findMissingSlow([3, 0, 1]))
    print(sol.findMissingFast([3, 0, 1]))
