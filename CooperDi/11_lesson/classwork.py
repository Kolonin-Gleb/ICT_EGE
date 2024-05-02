# Task 9 and 26 var 2


# Task 13
'''
from ipaddress import ip_network

counter = 0
for ip in ip_network('112.208.0.0/255.255.128.0', strict=False):
    adr = bin(int(ip))[2:]
    if adr.count('1') % 11 == 0:
        counter += 1
    
print(counter) # 3003
'''

# Task 6
'''
from turtle import *
# Настройка
screensize(4000, 4000)
tracer(0)
left(90)
k = 20

# Перемещение - Границы
for i in range(2):
    forward(23*k)
    left(90)
    backward(27*k)
    left(90)
penup()
backward(5*k)
right(90)
forward(11*k)
left(90)
pendown()
for i in range(2):
    forward(26*k)
    right(90)
    forward(32*k)
    right(90)
# Сетка
penup()
for x in range(-20, 50):
    for y in range(-20, 40):
        setpos(x*k, y*k)
        dot(5, 'blue')

done()
'''

