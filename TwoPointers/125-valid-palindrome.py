"""
125. Valid Palindrome
Difficulty: Easy
Topic: Two Pointers, String

Description:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Описание:
Фраза является палиндромом, если после удаления всех пробелов и знаков препинания и приведения к нижнему регистру она читается одинаково слева направо и справа налево.
Верни True, если s — палиндром.

Example:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""

from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        
        for i in s:
            if i.isalnum():
                new_s += i.lower()
                
        left = 0
        right = len(new_s) - 1
        
        flag = True
        while left < right:
            if new_s[left] != new_s[right]:
                flag = False
                break
            left += 1
            right -= 1
                
        
        return flag
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("A man, a plan, a canal: Panama"))