# 14948
'''
from ipaddress import ip_network

counter = 0

for ip in ip_network('192.168.32.128/255.255.255.192'):
    adr = bin(int(ip))[2:]
    if adr.count('1') % 2 == 0:
        counter += 1

print(counter) # 32
'''

# 14650
'''
'''

# TODO: 12947
'''
from ipaddress import ip_network

counter = 0
for ip in ip_network('203.111.195.0/255.255.240.0'): # 203.111.195.0/20 has host bits set
    adr = bin(int(ip))[2:]
    if adr.count('0') % 3 == 0 and adr.count('111000') >= 1:
        counter += 1

print(counter)
'''

# 12922
'''
from ipaddress import ip_network

counter = 0
for ip in ip_network('136.36.240.16/255.255.255.248'):
    adr = bin(int(ip))[2:]
    if adr.count('101') == 0:
        counter += 1

print(counter) # 4
'''


# 12467
'''
from ipaddress import ip_network

counter = 0
for A in range(0, 256):
    flag = True
    for ip in ip_network(f'183.192.{A}.0/255.255.252.0'): # 183.192.1.0/22 has host bits set
        adr = bin(int(ip))[2:]
        if adr[16:].count('1') > 3:
            flag = False
    if flag:
        print(A)
        break

print(counter) # 
'''



