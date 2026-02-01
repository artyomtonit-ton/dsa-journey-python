"""
1470. Shuffle the Array
Difficulty: Easy
Topic: Arrays

Description:
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Описание:
Дан массив, который условно разделен на две равные части: X и Y.
Нужно перемешать элементы так, чтобы они шли через один: x1, y1, x2, y2 и так далее.

Example:
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
"""

from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first_half = nums[:n]
        second_half = nums[n:]
        result = []

        for i in range(n):
            result.append(first_half[i])
            result.append(second_half[i])

        return result

if __name__ == "__main__":
    sol = Solution()
    print(sol.shuffle([2, 5, 1, 3, 4, 7], 3))