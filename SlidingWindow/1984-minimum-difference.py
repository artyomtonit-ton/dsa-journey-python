"""
1984. Minimum Difference Between Highest and Lowest of K Scores
Difficulty: Easy
Topic: Sliding Window, Sorting

Description:
You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.
Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.
Return the minimum possible difference.

Описание:
Дан массив nums. Нужно выбрать k чисел так, чтобы разница между Максимумом и Минимумом среди них была минимальной.

Example:
Input: nums = [9,4,1,7], k = 2
Output: 2
Explanation: Sorted: [1,4,7,9]. Pairs: (4-1)=3, (7-4)=3, (9-7)=2. Min is 2.
"""

from typing import List

class Solution:
    def minDiff(self, nums: List[int], k: int) -> int:

        nums.sort(reverse=True)

        curent_list = nums[:k]
        curent = curent_list[0] - curent_list[-1]

        minimal_difference = curent

        for i in range(k, len(nums)+1): 
            curent_list = nums[i-k:i]
            curent = curent_list[0] - curent_list[-1]

            if curent < minimal_difference:
                minimal_difference = curent 

        return minimal_difference 
              
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minDiff([9, 4, 1, 7], 2))
    print(sol.minDiff([9, 4, 1, 7, 10], 3))