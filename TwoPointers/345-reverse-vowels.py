"""
345. Reverse Vowels of a String
Difficulty: Easy
Topic: Two Pointers, String

Description:
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Описание:
Разверни только гласные буквы в строке ('a', 'e', 'i', 'o', 'u').
Остальные символы должны остаться на своих местах.
Регистр букв сохраняется.

Example:
Input: s = "IceCreAm"
Output: "AceCreIm"
"""

from typing import List

class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        s_list = list(s)

        left = 0
        right = len(s_list) - 1

        while left < right:
            if s_list[left] not in vowels:
                left += 1           
            elif s_list[right] not in vowels:
                right -= 1
            else:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1

        return "".join(s_list) 
              
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseVowels("IceCreAm"))
    print(sol.reverseVowels("hello"))