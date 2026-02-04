"""
349. Intersection of Two Arrays
Difficulty: Easy
Topic: Hash Table

Description:
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must be unique and you may return the result in any order.

Описание:
Даны два массива nums1 и nums2.
Верни список элементов, которые есть и в первом, и во втором массиве (пересечение).
Элементы в ответе должны быть уникальными.

Example:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
"""

from typing import List

class Solution:
    def intersectionArrays(self, nums1: List[int], nums2: list[int]) -> List[int]:
        return list(set(nums1) & set(nums2))

if __name__ == "__main__":
    sol = Solution()
    print(sol.intersectionArrays([1, 2, 2, 1], [2, 2]))