"""
14. Longest Common Prefix
Difficulty: Easy
Topic: Strings

Description:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Описание:
Найди самый длинный общий префикс (начало) среди массива строк.
Если общего префикса нет, верни пустую строку.

Example:
Input: strs = ["flower","flow","flight"]
Output: "fl"
"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        strs.sort()
        
        first = strs[0]
        last = strs[-1]
        
        idx = 0

        while idx < len(first) and idx < len(last):
            if first[idx] == last[idx]:
                idx += 1
            else:
                break
                
        return first[:idx]

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["flower", "flow", "flight"]))
    print(sol.longestCommonPrefix(["dog", "racecar", "car"]))