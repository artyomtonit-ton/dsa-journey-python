"""
1207. Unique Number of Occurrences
Difficulty: Easy
Topic: Hash Table

Description:
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique.

Описание:
Дан массив arr. Верни True, если количество повторений каждого числа уникально.
Пример: 1 встречается 3 раза, 2 встречается 2 раза. 3 != 2. Уникально.

Example:
Input: arr = [1,2,2,1,1,3]
Output: true
"""

from typing import List

class Solution:
    def isuniqueNumber(self, arr: List[int]) -> bool:
        dct = {}
        
        for i in arr:
            if i not in dct:
                dct[i] = 0
            dct[i] += 1
            
        return len(set(dct.values())) == len(dct.values())
            
        
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.isuniqueNumber([1, 2, 2, 1, 1, 3]))