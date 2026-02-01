"""
1689. Partitioning Into Minimum Number Of Deci-Binary Numbers
Difficulty: Medium (Logic: Easy)
Topic: Math, Greedy

Description:
A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros.
Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.

Описание:
"Deci-binary" число состоит только из цифр 0 и 1 (например, 101, 11).
Дана строка n (число). Найди минимальное количество deci-binary чисел, которые в сумме дадут n.

Example:
Input: n = "32"
Output: 3
Explanation: 10 + 11 + 11 = 32.
"""

from typing import List

class Solution:
    def finddecibinary(self, n: str) -> int:
        max_n = 0
        
        for i in n:
            if int(i) > max_n:
                max_n = int(i)
                
        return max_n
       

if __name__ == "__main__":
    s = Solution()
    print(s.finddecibinary("32"))