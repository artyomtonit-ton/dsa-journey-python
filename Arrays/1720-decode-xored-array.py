"""
1720. Decode XORed Array
Difficulty: Easy
Topic: Bit Manipulation (XOR)

Description:
There is a hidden integer array arr that consists of n non-negative integers.
It was encoded into another integer array encoded of length n - 1, such that encoded[i] = arr[i] XOR arr[i + 1].
You are given the encoded array and an integer first, that is the first element of arr, i.e. arr[0].
Return the original array arr.

Описание:
Дан массив encoded, который был получен из исходного массива arr с помощью операции XOR соседних элементов.
Мы знаем первый элемент исходного массива (first).
Нужно восстановить весь исходный массив.
Свойство: Если a ^ b = c, то a ^ c = b.

Example:
Input: encoded = [1,2,3], first = 1
Output: [1,0,2,1]
"""

from typing import List

class Solution:
    def decodeArray(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        
        for i in encoded:
            new_val = arr[-1] ^ i
            arr.append(new_val)
           
        return arr     

if __name__ == "__main__":
    s = Solution()
    print(s.decodeArray([1, 2, 3], 1))
