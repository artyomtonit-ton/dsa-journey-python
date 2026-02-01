"""
1431. Kids With the Greatest Number of Candies
Difficulty: Easy
Topic: Arrays, Greedy

Description:
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies.
Return a boolean array result where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Описание:
Есть массив candies (конфеты у детей) и число extraCandies (лишние конфеты).
Для каждого ребенка нужно проверить: если дать ему все лишние конфеты, станет ли у него их больше или столько же, сколько у САМОГО богатого ребенка в данный момент?
Верни список True/False.

Example:
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true]
Explanation: 
Kid 1 has 2 + 3 = 5 candies, which is >= max(2,3,5,1,3). Result is True.
Kid 4 has 1 + 3 = 4 candies, which is < max(5). Result is False.
"""

from typing import List

class Solution:
    def findcountextracandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        list_bool = []
        
        for i in candies:
            if i + extraCandies >= maxCandies:
                list_bool.append(True)
            else:
                list_bool.append(False)
            
        return list_bool

       

if __name__ == "__main__":
    s = Solution()
    print(s.findcountextracandies([2, 3, 5, 1, 3], 3))