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
Explanation: "e" occurs in both "leet" and "code".
"""

words = ["leet", "code", "cat", "home"]
x = "e"

def find_indexes(words, e):
    list_indexes = []

    for i in range(len(words)):
        if x in words[i]:
            list_indexes.append(i)

    return list_indexes

print(find_indexes(words, x))