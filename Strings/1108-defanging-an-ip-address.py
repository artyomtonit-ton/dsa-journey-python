"""
1108. Defanging an IP Address
Difficulty: Easy
Topic: Strings

Description:
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".

Описание:
Дана строка с IP-адресом.
Нужно заменить каждую точку "." на "[.]". Это часто делается для безопасности, чтобы ссылки не были кликабельными.

Example:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
"""

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