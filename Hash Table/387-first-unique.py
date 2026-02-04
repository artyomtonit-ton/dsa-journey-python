"""
387. First Unique Character in a String
Difficulty: Easy
Topic: Hash Table, Queue

Description:
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Описание:
Дана строка s. Найди первый символ, который не повторяется, и верни его индекс.
Если такого символа нет, верни -1.

Example:
Input: s = "leetcode"
Output: 0
"""

from typing import List

class Solution:
    def firstUnique(self, s: str) -> int:
        dct = {}
        
        for i in s:
            if i not in dct:
                dct[i] = 0
            dct[i] += 1
            
        for i in range(len(s)):
            if dct[s[i]] == 1:
                return i
            
        return -1
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.firstUnique("leetcode"))