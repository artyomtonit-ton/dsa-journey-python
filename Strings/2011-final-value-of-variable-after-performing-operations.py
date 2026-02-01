"""
2011. Final Value of Variable After Performing Operations
Difficulty: Easy
Topic: Strings, Arrays

Description:
There is a programming language with only four operations and one variable X:
++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0. Given an array of strings operations, return the final value of X.

Описание:
Есть переменная X, изначально равная 0.
Дан список операций.
Операции "++X" и "X++" увеличивают X на 1.
Операции "--X" и "X--" уменьшают X на 1.
Верни итоговое значение X.

Example:
Input: operations = ["--X","X++","X++"]
Output: 1
"""

from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0

        for op in operations:
            if "+" in op:
                x += 1
            else:
                x -= 1
        
        return x

if __name__ == "__main__":
    sol = Solution()
    print(sol.finalValueAfterOperations(["--x", "x++", "++x"]))