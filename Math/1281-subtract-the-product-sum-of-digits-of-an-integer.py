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
"""

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digit_sum = 0
        digit_prod = 1

        for char_digit in str(n):
            digit = int(char_digit)
            digit_sum += digit
            digit_prod *= digit

        return digit_prod - digit_sum

if __name__ == "__main__":
    s = Solution()
    print(s.subtractProductAndSum(234))