"""
217. Contains Duplicate
Difficulty: Easy
Topic: Hash Table

Description:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Описание:
Дан массив чисел nums. Верни True, если хотя бы одно число встречается дважды (есть дубликаты).
Верни False, если все числа уникальны.

Example:
Input: nums = [1,2,3,1]
Output: true
"""

from typing import List

class Solution:
    def isDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
       

if __name__ == "__main__":
    s = Solution()
    print(s.isDuplicate([1, 2, 3]))
    print(s.isDuplicate([1, 2, 3, 1]))
