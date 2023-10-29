# Task 1. Перевести 32 битный IP адрес ПК в 10 с.с.

# Так для каждого разряда
# print(int('11100000', 2))


# Task 2. Перевести 32 битный IP адрес ПК в 2 с.с.
'''
print(bin(222)[2:].zfill(8))
print(bin(37)[2:].zfill(8))
print(bin(12)[2:].zfill(8))
print(bin(108)[2:].zfill(8))
'''

# .zfill(8) - Добавить незначащие нули.
# Срава 0 до момента, пока чисел не станет 8
'''
print(int('11100000', 2)) # 224
print(int('00011000', 2)) # 24  
print(int('11100000', 2)) # 224
print(int('00000000', 2)) # 0
'''


# Task 6

# IP 208.240.112.208
# Маска 
# Адрес 208.240.112.192



# Homework

# Task 1
'''
print(int('11100100', 2)) # 228
print(int('01001110', 2)) # 78
print(int('10010101', 2)) # 149
print(int('11010000', 2)) # 208
'''

# Answer: 22878149208

# Task 2
'''
print(bin(100)[2:].zfill(8))
print(bin(125)[2:].zfill(8))
print(bin(214)[2:].zfill(8))
print(bin(0)[2:].zfill(8))
'''

# Answer: 01100100011111011101011000000000

# Task 3
"""
ip_address = ''

ip_address += bin(168)[2:].zfill(8)
ip_address += bin(240)[2:].zfill(8)
ip_address += bin(179)[2:].zfill(8)
ip_address += bin(255)[2:].zfill(8)

mask = ''

mask += bin(255)[2:].zfill(8)
mask += bin(255)[2:].zfill(8)
mask += bin(240)[2:].zfill(8)
mask += bin(0)[2:].zfill(8)

#############################

ip_digs = list(map(int, ip_address))
mask_digs = list(map(int, mask))

network_address = ''

for ip_dig, mask_dig in zip(ip_digs, mask_digs):
    network_address += str(ip_dig * mask_dig)


print(ip_address)
print(mask)
print(network_address)

print(int(network_address[:8], 2))
print(int(network_address[8:16], 2))
print(int(network_address[16:24], 2))
print(int(network_address[24:], 2))
"""

# Task 4
"""
ip_address = ''

ip_address += bin(220)[2:].zfill(8)
ip_address += bin(8)[2:].zfill(8)
ip_address += bin(232)[2:].zfill(8)
ip_address += bin(250)[2:].zfill(8)

mask = ''

mask += bin(255)[2:].zfill(8)
mask += bin(255)[2:].zfill(8)
mask += bin(224)[2:].zfill(8)
mask += bin(0)[2:].zfill(8)

#############################

ip_digs = list(map(int, ip_address))
mask_digs = list(map(int, mask))

network_address = ''

for ip_dig, mask_dig in zip(ip_digs, mask_digs):
    network_address += str(ip_dig * mask_dig)


print(ip_address)
print(mask)
print(network_address)

print(int(network_address[:8], 2))
print(int(network_address[8:16], 2))
print(int(network_address[16:24], 2))
print(int(network_address[24:], 2))
"""

# Task 5
'''
# Для узла с 
# IP-адресом = 250.128.197.17
# 3 байт IP-адреса = 197
print(bin(197)[2:].zfill(8))

# адрес сети = 250.128.192.0. 
# 3 байт адреса сети = 192
print(bin(192)[2:].zfill(8))

# В ответ запишите сумму единиц во всех возможных 
# вариантах представления третьего слева байта маски.
# Подсчёт на бумаге: ответ - 14
'''

# Task 6
'''
Для узла с IP-адресом 200.249.85.230 адрес сети равен 192.248.0.224.
Чему равно наибольшее возможное значение последнего (самого правого) байта маски?
Ответ запишите в виде десятичного числа.

print(bin(230)[2:].zfill(8))
print(bin(224)[2:].zfill(8))
# 11111000 - Макс. байт маски

print(int('11111000', 2)) # 248
'''

# Task 7
'''
'''

# Маска имеет уникальный разряд лишь в последнем байте, поэтому с последними байтами и работаем.
ip_address = ''
ip_address += bin(240)[2:].zfill(8)

mask = ''
mask += bin(248)[2:].zfill(8)

#############################
ip_digs = list(map(int, ip_address))
mask_digs = list(map(int, mask))

network_address = ''
for ip_dig, mask_dig in zip(ip_digs, mask_digs):
    network_address += str(ip_dig * mask_dig)

print(ip_address)
print(mask)
print(network_address)
print(int(network_address[:8], 2))

# Поэтому 2^4 / 2 = 8
# Однако система не принимает такой ответ.
