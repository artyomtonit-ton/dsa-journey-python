"""
1. Two Sum
Difficulty: Easy
Topic: Hash Table

Description:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Описание:
Дан массив nums и число target. Найди индексы двух чисел, сумма которых равна target.
Решение должно быть O(n) по времени.
Используем словарь (hash map), чтобы запоминать числа, которые мы уже видели, и их индексы.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)   
                    
        return res 

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
