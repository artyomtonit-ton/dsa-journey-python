"""
283. Move Zeroes
Difficulty: Easy
Topic: Two Pointers, Array

Description:
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Описание:
Дан массив nums. Перемести все нули в конец, сохраняя порядок остальных чисел.
Сделай это in-place (не создавая копию массива).

Example:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        insert_pos = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                insert_pos += 1
        
        for i in range(insert_pos, len(nums)):
            nums[i] = 0
        
        return nums
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.moveZeroes([0, 1, 0, 3, 12]))