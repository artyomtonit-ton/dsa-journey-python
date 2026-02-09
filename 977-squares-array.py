"""
977. Squares of a Sorted Array
Difficulty: Easy
Topic: Two Pointers, Sorting

Description:
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Описание:
Дан отсортированный массив nums (могут быть отрицательные числа).
Верни отсортированный массив квадратов этих чисел.
Хитрость: самые большие квадраты всегда по краям. Используй два указателя, сходящихся к центру, и заполняй результат с конца.

Example:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
"""

from typing import List

class Solution:
    def squaresArray(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        
        res = [0] * len(nums)
        
        for i in range(len(nums)-1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left]**2
                left += 1
            else:
                res[i] = nums[right]**2
                right -= 1
                
        return res
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.squaresArray([-4, -1, 0, 3, 10]))