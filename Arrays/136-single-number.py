"""
136. Single Number
Difficulty: Easy
Topic: Bit Manipulation (XOR)

Description:
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Описание:
В массиве все числа встречаются по два раза, кроме одного. Найди это одинокое число.
Используем операцию XOR (^).
Свойство: a ^ a = 0. Все пары уничтожатся, останется уникальное число.

Example:
Input: nums = [4,1,2,1,2]
Output: 4
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        
        for x in nums:
            res ^= x
        
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber([4, 1, 2, 1, 2]))
