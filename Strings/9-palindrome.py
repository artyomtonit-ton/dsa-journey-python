"""
9. Palindrome Number
Difficulty: Easy
Topic: Math

Description:
Given an integer x, return true if x is a palindrome, and false otherwise.
A palindrome reads the same backward as forward.

Описание:
Дано число x. Верни True, если число является палиндромом (читается одинаково слева направо и справа налево), иначе False.
Например, 121 — палиндром, а -121 — нет (из-за минуса).

Example:
Input: x = 121
Output: true
"""

from typing import List

class Solution:
    def palindromeNum(self, num: int) -> bool:
        return str(num) == str(num)[::-1]

if __name__ == "__main__":
    s = Solution()
    print(s.palindromeNum(121))
    print(s.palindromeNum(138))
