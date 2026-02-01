"""
2942. Find Words Containing Character
Difficulty: Easy
Topic: Arrays, Strings

Description:
You are given a 0-indexed array of strings words and a character x.
Return an array of indices representing the words that contain the character x.

Описание:
Дан список слов words и буква x.
Верни список индексов тех слов, в которых встречается буква x.

Example:
Input: words = ["leet","code"], x = "e"
Output: [0,1]
"""

from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        indices = []

        for i in range(len(words)):
            if x in words[i]:
                indices.append(i)

        return indices

if __name__ == "__main__":
    sol = Solution()
    print(sol.findWordsContaining(["leet", "code", "cat", "home"], "e"))