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
    def maxAvgSubarray(self, nums: List[int], k: int) -> int:
        
        curent_sum = sum(nums[:k])
        max_avg = curent_sum

        for i in range(k, len(nums)): 
            curent_sum += nums[i] - nums[i - k]

            if curent_sum  > max_avg:
                max_avg = curent_sum

        return max_avg / k
              
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxAvgSubarray([1, 12, -5, -6, 50, 3], 4))