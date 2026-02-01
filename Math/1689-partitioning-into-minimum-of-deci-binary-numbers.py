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
"""

class Solution:
    def minPartitions(self, n: str) -> int:
        max_digit = 0
        
        for char in n:
            digit = int(char)
            if digit > max_digit:
                max_digit = digit
                
        return max_digit

if __name__ == "__main__":
    s = Solution()
    print(s.minPartitions("32"))