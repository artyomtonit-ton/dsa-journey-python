"""
1221. Split a String in Balanced Strings
Difficulty: Easy
Topic: Strings, Greedy

Description:
Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
Given a balanced string s, split it into some number of substrings such that:
Each substring is balanced.
Return the maximum number of balanced strings you can obtain.

Описание:
Сбалансированная строка содержит равное количество символов 'L' и 'R'.
Дана строка s. Нужно разбить её на максимальное количество подстрок, каждая из которых тоже сбалансирована.
Верни это количество.

Example:
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
"""

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        ans = 0
        
        for char in s:
            if char == 'R':
                balance += 1
            else:
                balance -= 1
    
            if balance == 0:
                ans += 1
                
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.balancedStringSplit("RLRRLLRLRL"))