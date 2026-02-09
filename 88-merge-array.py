"""
88. Merge Sorted Array
Difficulty: Easy
Topic: Two Pointers, Array

Description:
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
Merge nums2 into nums1 as one sorted array.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1.

Описание:
Даны два отсортированных массива nums1 и nums2.
В nums1 есть место в конце (нули) для элементов из nums2.
Нужно слить nums2 в nums1 так, чтобы результат остался отсортированным.
Делаем это in-place (без создания нового массива).

Example:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
"""

from typing import List

class Solution:
    def mergeArray(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        
        while p2 >= 0:
            if  p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1   
            else: 
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        return nums1
              
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.mergeArray([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))