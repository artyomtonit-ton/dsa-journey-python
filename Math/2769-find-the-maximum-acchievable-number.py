"""
2769. Find the Maximum Achievable Number
Difficulty: Easy
Topic: Math, Logic

Description:
Given two integers, num and t.
You can increase or decrease num by 1, t times.
You can increase or decrease an unknown number x by 1, t times.
Find the maximum possible value of x that can become equal to num.

Описание:
Даны два числа num и t.
Мы можем изменить num на 1 ровно t раз (например, увеличить).
Одновременно с этим неизвестное число x тоже меняется на 1 ровно t раз (например, уменьшается).
Найди максимальное возможное x, которое сможет встретиться с num после этих операций.

Example:
Input: num = 4, t = 1
Output: 6
Explanation: The maximum achievable number is x = 6; it can become equal to num after performing the decrease operation once.
"""
"""
2769. Find the Maximum Achievable Number
Difficulty: Easy
Topic: Math, Logic

Description:
Given two integers, num and t.
You can increase or decrease num by 1, t times.
You can increase or decrease an unknown number x by 1, t times.
Find the maximum possible value of x that can become equal to num.

Описание:
Даны два числа num и t.
Мы можем изменить num на 1 ровно t раз (например, увеличить).
Одновременно с этим неизвестное число x тоже меняется на 1 ровно t раз (например, уменьшается).
Найди максимальное возможное x, которое сможет встретиться с num после этих операций.

Example:
Input: num = 4, t = 1
Output: 6
Explanation: The maximum achievable number is x = 6; it can become equal to num after performing the decrease operation once.
"""

from typing import List

class Solution:
    def findMaxAcchievableNum(self, num: int, t: int) -> int:
        return num + (t * 2)
       

if __name__ == "__main__":
    s = Solution()
    print(s.findMaxAcchievableNum(4, 1))
    print(s.findMaxAcchievableNum(4, 2))