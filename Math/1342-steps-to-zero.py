"""
1342. Number of Steps to Reduce a Number to Zero
Difficulty: Easy
Topic: Math, Bit Manipulation

Description:
Given an integer num, return the number of steps to reduce it to zero.
In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

Описание:
Дано число num. Нужно посчитать количество шагов, чтобы превратить его в 0.
Правила шагов:
- Если число четное — раздели его на 2.
- Если число нечетное — вычти из него 1.

Example:
Input: num = 14
Output: 6
"""

class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num != 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            steps += 1
        
        return steps

if __name__ == "__main__":
    s = Solution()
    print(s.numberOfSteps(14))