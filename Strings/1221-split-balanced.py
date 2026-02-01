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
Дана сбалансированная строка s (поровну 'L' и 'R').
Нужно разрезать её на максимальное количество кусков, чтобы каждый кусок тоже был сбалансированным.

Example:
Input: s = "RLRRLLRLRL"
Output: 4
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