"""
771. Jewels and Stones
Difficulty: Easy
Topic: Strings, Hash Table

Description:
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have.
Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Описание:
Дана строка jewels (типы драгоценностей) и строка stones (камни, которые у тебя есть).
Нужно посчитать, сколько камней из stones являются драгоценностями (то есть входят в jewels).
Регистр важен ("a" и "A" — разные камни).

Example:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Explanation: "a", "A", "A" are jewels. Total 3.
"""

from typing import List

class Solution:
    def findCountJewels(self, jewels: str, stones: str) -> int:
        count_jewels = 0
        for i in stones:
            if i in jewels:
                count_jewels += 1

        return count_jewels
       

if __name__ == "__main__":
    s = Solution()
    print(s.findCountJewels("aA", "aAAbbbb"))