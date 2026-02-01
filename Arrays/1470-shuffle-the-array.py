"""
1470. Shuffle the Array
Difficulty: Easy
Topic: Arrays

Description:
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Описание:
Дан массив, который условно разделен на две равные части: X и Y.
Нужно перемешать элементы так, чтобы они шли через один: x1, y1, x2, y2 и так далее.

Example:
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
Explanation: [2,5,1] interleaved with [3,4,7].
"""

n = 3
nums = [2, 5, 1, 3, 4, 7]


def shuffle(n, nums):
    list_X = nums[:n]
    list_y = nums[n:]
    x_y = []

    for i in range(n):
        x_y.append(list_X[i])
        x_y.append(list_y[i])

    return x_y

print(shuffle(n, nums))