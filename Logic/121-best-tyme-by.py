"""
121. Best Time to Buy and Sell Stock
Difficulty: Easy
Topic: Array, Sliding Window

Description:
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Описание:
Дан массив цен на акции. Нужно выбрать один день для покупки и один (будущий) день для продажи, чтобы получить макс. прибыль.
Верни максимальную прибыль.

Example:
Input: prices = [7,1,5,3,6,4]
Output: 5
"""

from typing import List

class Solution:
    def bestTimeBySell(self, prices: List[str]) -> int:
        max_num = max(prices)
        n = 0

        while True:
            if prices[0] != max_num:
                return max_num - min(prices[:prices.index(max_num)])
            else:
                n += 1
                max_num = max(prices[n:])
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.bestTimeBySell([7, 1, 5, 3, 6, 4]))
