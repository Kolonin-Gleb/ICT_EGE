# Task 2
'''
print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ( (x and (not z)) or (y == z) or (not w) ) == 0:
                    print(x, y, z, w)
'''
"""
x y z w
0 0 1 1
0 1 0 1
1 0 1 1
"""

# Task 4
'''
for N in range(1_000):
    N_2 = bin(N)[2:]
    R_2 = ''

    if N % 2 == 0:
        R_2 = N_2 + '01'
    else:
        R_2 = '1' + N_2 + '1'

    R = int(R_2, 2)

    if R > 156:
        print(N) # 33
        break
'''


# Task 5
'''
from turtle import *
# Настройка
screensize(3000, 3000)
tracer(0)
left(90)
k = 40

# Перемещения
for i in range(2):
    forward(13*k)
    right(90)
    forward(18*k)
    right(90)

penup()

forward(5*k)
right(90)
forward(9*k)
left(90)

pendown()

for i in range(2):
    forward(11*k)
    right(90)
    forward(7*k)
    right(90)
    
# Сетка
penup()
for x in range(-10, 30):
    for y in range(-10, 30):
        setpos(x*k, y*k)
        dot(5, 'blue')

done()
'''

# Task 8
'''
num = 0
for b1 in sorted("ПАРУС"):
    for b2 in sorted("ПАРУС"):
        for b3 in sorted("ПАРУС"):
            for b4 in sorted("ПАРУС"):
                for b5 in sorted("ПАРУС"):
                    num += 1
                    word = b1+b2+b3+b4+b5
                    if word.count("У") <= 1 and word.count("АА") == 0:
                        print(num, word)
                        exit()
# 131 АПАПА
'''

# Задание 10 заметки
'''
по и По - всего = 794
по и По - как слово = 60
Результат = 1ое - 2ое = 734
'''

# Task 12
'''
s = '8'*45

while '1111' in s or '8888' in s:
    if '1111' in s:
        s = s.replace('1111', '88', 1)
    else:
        s = s.replace('8888', '11', 1)

print(s) #888
'''

# Task 14
'''
def dec_to_27(n):
    res = []

    while n > 0:
        res.append(n % 27)
        n //= 27
    
    return res

num = 3 * 2187**2020 + 3 * 729**2021 - 2 * 81**2022 + 27**2023 - 4*3**2024 - 2029

res = dec_to_27(num)
# print(res)
counter = 0

for el in res:
    if el > 9:
        counter += 1

print(counter) # 3368
'''

# Task 14 another one =)
'''
'''


# Task 15 
'''
for A in range(1, 10_000): # 1 - чтобы избежать деления на 0
    flag = True
    for x in range(1000):
        if ( (x % A != 0) <= ( (x % 28 == 0) <= (x % 49 != 0) ) ) != 1:
            flag = False
            break
    
    if flag:
        print(A) # max = 196
'''

# Task 15 another one =)
'''
'''

# Task 16
'''
import sys
sys.setrecursionlimit(9999)

def F(n):
    if n <= 7:
        return 1
    return n + 2 + F(n - 1)


print(F(2024) - F(2020)) # 8098
'''











