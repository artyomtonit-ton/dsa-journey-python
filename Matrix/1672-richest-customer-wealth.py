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
Explanation: Both customers have wealth = 6.
"""

accounts = [
    [1, 2, 3],
    [3, 2, 1],
    [3, 6, 1, 4]
]

def find_max_wealth(accounts):
    max_wealth = sum(accounts[0])

    for i in accounts:
        if sum(i) > max_wealth:
            max_wealth = sum(i)

    return max_wealth

print(find_max_wealth(accounts))
