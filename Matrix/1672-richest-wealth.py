"""
1672. Richest Customer Wealth
Difficulty: Easy
Topic: Matrix

Description:
You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i-th customer has in the j-th bank.
Return the wealth that the richest customer has.
A customer's wealth is the amount of money they have in all their bank accounts.

Описание:
Дана матрица accounts.
Каждая строка — это клиент. Числа в строке — это деньги на разных счетах этого клиента.
Нужно посчитать сумму денег для каждого клиента и вернуть максимальную из этих сумм (богатство самого богатого).

Example:
Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
"""

from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = sum(accounts[0])

        for customer_accounts in accounts:
            if sum(customer_accounts) > max_wealth:
                max_wealth = sum(customer_accounts)

        return max_wealth

if __name__ == "__main__":
    sol = Solution()
    accounts = [
        [1, 2, 3],
        [3, 2, 1],
        [3, 6, 1, 4]
    ]
    print(sol.maximumWealth(accounts))
