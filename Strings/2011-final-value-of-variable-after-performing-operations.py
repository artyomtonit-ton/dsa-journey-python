operations = ["--x", "x++", "++x"]

def find_x(prtns):
    x = 0

    for i in prtns:
        if "+" in i:
            x += 1
        else:
            x -= 1
    
    return x

print(find_x(operations))