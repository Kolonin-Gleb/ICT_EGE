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

# Task 7 and 8
'''
В файлах 7.png и 8.png
соответственно
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
по и По - как слово = 60 - 5 (5 где по с дефисом) = 55
Результат = 1ое - 2ое = 739

ОШИБКА!
WORD находит по как отдельное слово, даже если после него стоит дефис
Пример: По-христиански
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

# Task 13
# ip  = '105.224.200.224'
# mask = '255.255.255.224'

# print(bin(224)[2:].zfill(8))
# print(bin(224)[2:].zfill(8))
# Тогда весь IP адрес будет:
# print(bin(105)[2:].zfill(8), bin(224)[2:].zfill(8), bin(200)[2:].zfill(8), bin(224)[2:].zfill(8))  # ip
# print(bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(255)[2:].zfill(8), bin(224)[2:].zfill(8))  # mask
'''
01101001 11100000 11001000 11100000  # ip = 13 единиц
11111111 11111111 11111111 11100000  # mask
# mask показывает, сколько значений может меняться в ip
# 00000 = 5 нулей => 5 значений
Чтобы стало кратно 4, нужно чтобы среди последних 5 нулей появислось = 3 единицы.
Позиции этих 1 не важны
'''
"""
count = 0
for d1 in '01':
    for d2 in '01':
        for d3 in '01':
            for d4 in '01':
                for d5 in '01':
                    num = d1+d2+d3+d4+d5
                    if num.count('1') == 3:
                        count += 1

print(count) # 10 -  количество ip адресов, кратных 4.
"""

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
for x in '0123456789ABCDEFGHIJKLMNOPQ'[::-1]: # требуют наиб. Х
    num = int(f"123{x}24", 27) + int(f"135{x}78", 27)
    if num % 26 == 0:
        print(num // 26) # 1213206
        break
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
Имею дело с отрезками. Нужно решать на "бумаге"!
Смотри файл 15.png
# Ответ: 43
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


# Task 17
# Опр. кол. пар последовательности,
# в которых хотя бы 1 число больше max_19
# Найдите максимальную из сумм эл. таких пар.
'''
f = open('17_15333.txt')
data = f.readlines()
data = list(map(int, data))
f.close()

max_19 = 0
for el in data:
    if el % 19 == 0:
        max_19 = max(el, max_19)

pair_counter = 0
max_pair_sum = 0

for i in range(len(data) - 1):
    if data[i] > max_19 or data[i + 1] > max_19:
        pair_counter += 1
        max_pair_sum = max(max_pair_sum, data[i] + data[i + 1])

print(pair_counter, max_pair_sum)
'''

# Task 19 Начинается Теория игр
'''
2 Кучи

Ходы:
+1
*2

a + b = S >= 123
a = 13
b = [1; 109] - включительно
'''

"""
def F(a, b, m):
    # усл. победы
    if a + b >= 123:
        return m % 2 == 0 # На чьём ходе победа
    # ходы кончились
    if m == 0:
        return 0 # победы достичь не удалось
    # Рассматриваем все ходы
    h = [F(a+1, b, m-1), F(a*2, b, m-1), F(a, b+1, m-1), F(a, b*2, m-1)]

    # Заученная фраза -- нифига не помню
    return any(h) if (m-1) % 2 == 0 else all(h) # all <-> any (any for unlucky move)

# В цикле перебираем кучу b и проверяем функцию на победу
print("19)", [b for b in range(1, 110) if F(13, b, 2)]) # min S = 28
print("20)", [b for b in range(1, 110) if not F(13, b, 1) and F(13, b, 3)]) #  48 54
print("21)", [b for b in range(1, 110) if not F(13, b, 2) and F(13, b, 4)]) # min S = 47 
"""

# Task 22
'''
Parallel Processes in Excel
'''

# Task 23
'''
# import sys
# sys.setrecursionlimit(9999)
# from functools import lru_cache
# @lru_cache()
def F(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return F(x+1, y) + F(x*2, y)

print(F(4, 8) * F(8, 10) * F(10, 15)) # 2
'''

# Task 24
'''
f = open('24_15339.txt')
line = f.readline()
# Замена всех букв на 0
line = line.replace('A', '0')
line = line.replace('B', '0')
line = line.replace('C', '0')
# Замена всех цифр на 1
line = line.replace('6', '1')
line = line.replace('7', '1')
line = line.replace('8', '1')
line = line.replace('9', '1')
f.close()

k = 1 # тек.  макс. последовательность
m = 1 # глоб. макс. последовательность

for i in range(len(line) - 1):
    if (line[i] == '0' and line[i+1] == '1') or (line[i] == '1' and line[i+1] == '0'):
        k += 1
    else:
        m = max(k, m)
        k = 1

m = max(k, m) # на  случай, если последний k не оборвётся и будет максимальным
print(m)
'''

# Task 25
"""
from fnmatch import fnmatch

for x in range(0, 10**10, 2024):
    if fnmatch(str(x), '1*2322?2'):
        print(x, x//2024)
"""
'''
158232272 78178
1100232232 543593
1170232272 578178
1353232232 668593
1423232272 703178
1606232232 793593
1676232272 828178
1859232232 918593
1929232272 953178
'''
