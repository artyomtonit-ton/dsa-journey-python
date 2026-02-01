"""
1512. Number of Good Pairs
Difficulty: Easy
Topic: Arrays, Hash Table

Description:
Given an array of integers nums, return the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Описание:
Пара индексов (i, j) считается "хорошей", если числа под этими индексами равны (nums[i] == nums[j]) и при этом i < j (первый индекс меньше второго).
Посчитай количество таких пар.

Example:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: Pairs are (0,3), (0,4), (3,4), (2,5).
"""

nums = [1, 2, 3, 1, 1, 3]

def find_goodpairs(nums):
    count = 0

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j] and i < j:
                count += 1
    
    return count

print(find_goodpairs(nums))