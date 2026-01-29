s = "hello"

def find_scorestr(s):
    score = 0
    for i in range(0, len(s)-1):
        score += abs(ord(s[i]) - ord(s[i+1]))

    return score

print(find_scorestr(s))