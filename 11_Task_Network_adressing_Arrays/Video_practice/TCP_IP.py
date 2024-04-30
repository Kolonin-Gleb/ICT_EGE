# Системы Счисления

# Task 1
'''
from ipaddress import ip_network

count = 0
for ip in ip_network('214.240.126.200/255.255.255.248'): # ip адрес которым задана сеть / маска
    # print(ip)
    # print(bin(int(ip))[2:])
    adr = bin(int(ip))[2:] # в 2 С.С.
    
    if adr.count('1') % 2 != 0:
        count += 1
    
print(count) # 4
'''
# Task 2
'''
from ipaddress import ip_network

count = 0
for ip in ip_network('200.100.219.192/255.255.255.224'): # ip адрес которым задана сеть / маска
    # print(ip)
    # print(bin(int(ip))[2:])
    adr = bin(int(ip))[2:] # в 2 С.С.
    
    if adr.count('1') % 2 == 0:
        count += 1
    
print(count) # 16
'''

# Task 3
'''
from ipaddress import ip_network

count = 0
for ip in ip_network('105.224.200.224/255.255.255.224'): # ip адрес которым задана сеть / маска
    # print(ip)
    # print(bin(int(ip))[2:])
    adr = bin(int(ip))[2:] # в 2 С.С.
    
    if adr.count('1') % 4 == 0:
        count += 1
    
print(count) # 10
'''







