accounts = [
    [1, 2, 3],
    [3, 2, 1],
    [3, 6, 1, 4]
]

def find_max_wealth(accounts):
    max_wealth = sum(accounts[0])

    for i in accounts:
        if sum(i) > max_wealth:
            max_wealth = sum(i)

    return max_wealth

print(find_max_wealth(accounts))
