address = "1.1.1.1"

def replace_address(address): 
    new_ip = ""
    for i in range(len(address)):
        if address[i] == ".":
            new_ip += "[.]"
        else:
            new_ip += address[i]
    
    return new_ip

print(replace_address(address))