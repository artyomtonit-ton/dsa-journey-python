"""
26. Remove Duplicates from Sorted Array
Difficulty: Easy
Topic: Two Pointers

Description:
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once.
Return the number of unique elements.

Описание:
Дан отсортированный массив nums. Удалить дубликаты на месте (in-place).
Нужно вернуть количество уникальных элементов k.
Первые k элементов массива должны быть уникальными.

Example:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        
        return slow + 1
        
if __name__ == "__main__":
    sol = Solution()
    k = sol.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    print(k)