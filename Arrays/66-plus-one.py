"""
66. Plus One
Difficulty: Easy
Topic: Arrays, Math

Description:
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
Increment the large integer by one and return the resulting array of digits.

Описание:
Дан массив цифр, представляющий число (например [1,2,3] -> 123).
Прибавь к числу 1 и верни результат в виде массива.
Учитывай, что 9 превращается в 10 (перенос разряда).

Example:
Input: digits = [1,2,9]
Output: [1,3,0]
"""

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for i in digits:
            s += str(i)
         
        number = int(s) + 1
        res_str = str(number)
        
        res = []
        for j in res_str:
            res.append(int(j))
        
        return res         
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([1, 2, 9]))