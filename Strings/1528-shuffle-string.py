"""
1528. Shuffle String
Difficulty: Easy
Topic: Arrays, Strings

Description:
You are given a string s and an integer array indices of the same length.
The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
Return the shuffled string.

Описание:
Дана строка s и массив индексов indices.
Нужно переместить каждый символ s[i] на позицию indices[i] в новой строке.
То есть, мы знаем, где должен стоять каждый символ в финале.

Example:
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
"""

from typing import List

class Solution:
    def shuffleString(self, s: str, indices: List[int]) -> str:
        shuffle_s = [""] * len(s)
        
        for i in range(len(s)):
            shuffle_s[indices[i]] += s[i]
            
        return "".join(shuffle_s)

if __name__ == "__main__":
    s = Solution()
    print(s.shuffleString("codeleet", [4, 5, 6, 7, 0, 1, 2, 3]))
    print(s.shuffleString("abc", [1, 2, 0]))
