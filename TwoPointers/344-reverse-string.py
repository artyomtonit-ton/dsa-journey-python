"""
344. Reverse String
Difficulty: Easy
Topic: Two Pointers, String

Description:
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.

Описание:
Разверни строку (массив символов) s задом наперед.
Сделай это in-place, используя два указателя.

Example:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""

from typing import List

class Solution:
    def reverse(self, s: List[str]) -> List[str]:
        left = 0
        right = len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            
            left += 1
            right -= 1
            
        return s
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.reverse(["h", "e", "l", "l", "o"]))