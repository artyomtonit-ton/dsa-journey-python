"""
1832. Check if the Sentence Is Pangram
Difficulty: Easy
Topic: Hash Table, String

Description:
A pangram is a sentence where every letter of the English alphabet appears at least once.
Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

Описание:
Панграмма — это предложение, содержащее все 26 букв английского алфавита.
Верни True, если строка является панграммой.

Example:
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
"""

from typing import List

class Solution:
    def isPangram(self, sentence: str) -> bool:
        dct = {}
        new_sentence = sentence.replace(".", "").lower()
        new_sentence = new_sentence.replace(" ", "")
        
        for i in new_sentence:
            if i not in dct:
                dct[i] = 0
            dct[i] += 1
            
        return len(dct) == 26
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.isPangram("The quick brown fox jumps over the lazy dog."))