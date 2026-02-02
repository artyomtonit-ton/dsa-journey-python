"""
169. Majority Element
Difficulty: Easy
Topic: Sorting, Hash Table

Description:
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Описание:
Дан массив nums размера n. Найди "мажоритарный" элемент.
Это элемент, который встречается чаще, чем n / 2 раз.
Самый простой способ: если отсортировать массив, мажоритарный элемент всегда будет стоять посередине.

Example:
Input: nums = [3,2,3]
Output: 3
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]

if __name__ == "__main__":
    s = Solution()
    print(s.majorityElement([3, 2, 3]))
