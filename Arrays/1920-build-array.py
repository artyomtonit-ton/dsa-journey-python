"""
1920. Build Array from Permutation
Difficulty: Easy
Topic: Arrays

Description:
Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

Описание:
Дан массив nums. Нужно построить новый массив ans такой же длины.
Правило заполнения: ans[i] должен быть равен nums[nums[i]].
То есть, значение элемента nums[i] служит индексом для получения нового значения.

Example:
Input: nums = [0,2,1,5,3,4]
Output: [0,1,2,4,5,3]
"""

from typing import List

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums) 

        for i in range(len(nums)):
            ans[i] = nums[nums[i]]

        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.buildArray([0, 2, 1, 5, 3, 4]))