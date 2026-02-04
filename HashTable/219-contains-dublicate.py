"""
219. Contains Duplicate II
Difficulty: Easy
Topic: Hash Table, Sliding Window

Description:
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Описание:
Дан массив nums и число k.
Верни True, если в массиве есть два одинаковых числа, стоящих не дальше чем в k шагах друг от друга (разница индексов <= k).

Example:
Input: nums = [1,2,3,1], k = 3
Output: true
"""

from typing import List

class Solution:
    def containsDublicate(self, nums: List[int], k: int) -> bool:
        dct = {}
        flag = False
        
        for i in range(len(nums)):
            if nums[i] not in dct:
                dct[nums[i]] = i
            elif nums[i] in dct:
                if abs(dct[nums[i]] - i) <= k:
                    flag = True
                    dct[nums[i]] = i
                            
        return flag
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDublicate([1, 2, 3, 1], 3))