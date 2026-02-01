"""
3110. Score of a String
Difficulty: Easy
Topic: Strings

Description:
You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.
Return the score of s.

Описание:
Дан строка s. "Счет" строки — это сумма модулей разности ASCII-кодов соседних символов.
Нужно пройтись по строке и сложить |s[i] - s[i+1]| для всех соседних пар.

Example:
Input: s = "hello"
Output: 13
Explanation: |h-e| + |e-l| + |l-l| + |l-o| = |104-101| + ... = 3 + 7 + 0 + 3 = 13.
"""

s = "hello"

def find_scorestr(s):
    score = 0
    for i in range(0, len(s)-1):
        score += abs(ord(s[i]) - ord(s[i+1]))

    return score

print(find_scorestr(s))