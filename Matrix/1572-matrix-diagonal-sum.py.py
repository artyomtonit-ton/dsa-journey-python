"""
1572. Matrix Diagonal Sum
Difficulty: Easy
Topic: Matrix

Description:
Given a square matrix mat, return the sum of the matrix diagonals.
Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

Описание:
Дана квадратная матрица mat.
Нужно посчитать сумму элементов на главной и побочной диагоналях.
Важно: Элемент в центре матрицы (если она нечетного размера) учитывается только ОДИН раз.

Example:
Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
"""

from typing import List
import numpy as np

class Solution:
    def diagonalSum(self, matrix: List[List]) -> int:
        sum = 0
        l = len(matrix)
        flip_matrix = np.fliplr(matrix)
        
        for i in range(l):
            sum += matrix[i][i]
            
        for i in range(l):
            sum += flip_matrix[i][i]
        
        if l % 2 != 0:
            sum -= matrix[l//2][l//2]
            
        return sum

if __name__ == "__main__":
    s = Solution()
    print(s.diagonalSum([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]]))
    
    print(s.diagonalSum([[1, 2, 3, 5],
                         [4, 5, 6, 9],
                         [7, 8, 9, 0],
                         [1, 1, 1, 1]]))
