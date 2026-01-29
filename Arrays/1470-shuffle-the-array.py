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