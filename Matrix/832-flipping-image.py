"""
832. Flipping an Image
Difficulty: Easy
Topic: Matrix, Bit Manipulation

Description:
Given an n x n binary matrix image, flip the image horizontally, then invert it, and return the resulting image.
To flip an image horizontally means that each row of the image is reversed.
To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0.

Описание:
Дана бинарная матрица (картинка).
Нужно сделать два действия:
1. Перевернуть каждую строку задом наперед (Reverse).
2. Инвертировать цвета (0 меняем на 1, 1 меняем на 0).

Example:
Input: image = [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
"""

from typing import List

class Solution:
    def flipping(self, matrix: List[List]) -> List[List]:
        arr = []
        
        for i in matrix:
            arr.append(i[::-1])
            
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                arr[i][j] = 1 - arr[i][j]
                    
        return arr

if __name__ == "__main__":
    s = Solution()
    print(s.flipping([[1, 1, 0],
                     [1, 0, 1],
                     [0, 0, 0]]))
