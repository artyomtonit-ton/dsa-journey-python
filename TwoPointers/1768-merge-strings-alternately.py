"""
1768. Merge Strings Alternately
Difficulty: Easy
Topic: Two Pointers, String

Description:
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, append the additional letters onto the end of the merged string.

Описание:
Даны две строки. Нужно объединить их, чередуя буквы: 1-я буква первой, 1-я второй, 2-я первой, 2-я второй и т.д.
Хвост длинной строки просто приклеивается в конец.

Example:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
"""

from typing import List

class Solution:
    def mergeStrungs(self, word1: str, word2: str) -> str:
        res = ""
        left = 0
        right = 0

        while left < len(word1) and right < len(word2):
            res += word1[left]
            res += word2[right]
            
            left += 1
            right += 1

        res += word1[left:]
        res += word2[right:]

        return res
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.mergeStrungs("abc", "pqr"))
