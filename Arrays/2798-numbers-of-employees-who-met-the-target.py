"""
2798. Number of Employees Who Met the Target
Difficulty: Easy
Topic: Arrays

Description:
There are n employees in a company, numbered from 0 to n - 1. Each employee i has worked hours[i] hours in the company.
The company requires each employee to work at least target hours.
Return the integer denoting the number of employees who met the target.

Описание:
Дан массив hours, где hours[i] — это часы работы i-го сотрудника.
Также дано число target (минимальная норма часов).
Посчитай количество сотрудников, которые отработали target часов или больше.

Example:
Input: hours = [0,1,2,3,4], target = 2
Output: 3
"""

from typing import List

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for h in hours:
            if h >= target:
                count += 1

        return count

if __name__ == "__main__":
    s = Solution()
    print(s.numberOfEmployeesWhoMetTarget([0, 1, 2, 3, 4], 2))