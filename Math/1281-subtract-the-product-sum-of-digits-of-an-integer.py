"""
1281. Subtract the Product and Sum of Digits of an Integer
Difficulty: Easy
Topic: Math

Description:
Given an integer number n, return the difference between the product of its digits and the sum of its digits.

Описание:
Дано целое число n.
Нужно вернуть разницу между произведением его цифр и суммой его цифр.
(Произведение - Сумма).

Example:
Input: n = 234
Output: 15
Explanation: 
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15
"""

from typing import List

class Solution:
    def subtractDigits(self, num: int) -> int:
        addition = 0
        multiplication = 1

        for i in str(num):
            addition += int(i)
            multiplication *= int(i)

        return multiplication - addition



if __name__ == "__main__":
    s = Solution()
    print(s.subtractDigits(234))