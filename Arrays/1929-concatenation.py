"""
1929. Concatenation of Array
Difficulty: Easy
Topic: Arrays

Description:
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
Specifically, ans is the concatenation of two nums arrays.

Описание:
Дан массив nums. Создай новый массив ans, который состоит из двух копий массива nums, склеенных друг с другом.
Длина нового массива будет в 2 раза больше исходного.

Example:
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
"""

from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums * 2 
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.getConcatenation([1, 2, 1]))