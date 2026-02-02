"""
242. Valid Anagram
Difficulty: Easy
Topic: Strings, Sorting

Description:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Описание:
Даны две строки s и t. Верни True, если t является анаграммой s.
Анаграмма — это слово, составленное из тех же букв, но в другом порядке.
Решение: если отсортировать буквы в обоих словах, списки должны стать идентичными.

Example:
Input: s = "anagram", t = "nagaram"
Output: true
"""

from typing import List

class Solution:
    def validAnagram(self, s: str, t: str) -> bool:
        return sorted(t) == sorted(s)

if __name__ == "__main__":
    s = Solution()
    print(s.validAnagram("anagram", "nagaram"))

