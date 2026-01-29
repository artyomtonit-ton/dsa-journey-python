words = ["leet", "code", "cat", "home"]
x = "e"

def find_indexes(words, e):
    list_indexes = []

    for i in range(len(words)):
        if x in words[i]:
            list_indexes.append(i)

    return list_indexes

print(find_indexes(words, x))