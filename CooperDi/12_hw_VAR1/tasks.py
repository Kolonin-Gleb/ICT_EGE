# TODO: Task 1 - board
# ---
# (33) был верным

# Task 2
'''
print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if (w and ((not x) or y) and ((not y) and z or y and (not z) ) ) == 1:
                    print(x, y, z, w)

"""
x y z w
0 0 1 1
0 1 0 1
1 1 0 1
"""
# ANSWER: yxzw +
'''

# Task 3 - Excel
# 403 +

# Task 4 - Excel
# 26 ------
# (29) был верным

# Task 5
'''
for N in range(10_000):
    N_2 = bin(N)[2:]
    R_2 = ''
    if N % 2 == 0:
        R_2 = N_2 + N_2[-2:]
    if N % 2 != 0:
        R_2 = '1' + N_2 + '0'
    R = int(R_2, 2)
    if R == 202:
        print(N) # 50 - max (+)
'''

# Task 6
'''
from turtle import *
screensize(1000, 1000)
tracer(0)
left(90)
k = 30

for i in range(2):
    forward(5*k)
    left(90)
    backward(13*k)
    left(90)
penup()
backward(10*k)
right(90)
forward(9*k)
left(90)
pendown()
for i in range(2):
    forward(11*k)
    right(90)
    forward(7*k)
    right(90)

penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x*k, y*k)
        dot(5, 'blue')

done() # 10 (+)
'''

# Task 7 - paper
'''
# print(2**14)
# print(1280*1024*14*70/12582912)
# 102.08333333333333
# Answer = 102 (+)
'''

# Task 8
'''
counter = 0
for d1 in '123456':
    for d2 in '0123456':
        for d3 in '0123456':
            for d4 in '0123456':
                for d5 in '0123456':
                    for d6 in '0123456':
                        num = d1+d2+d3+d4+d5+d6
                        if num.count('3') == 1:
                            # num = num.replace('0', '*').replace('2', '*').replace('4', '*').replace('6', '*')
                            num = num.replace('1', '+').replace('3', '+').replace('5', '+')
                            if num.count('++') == 0:
                                counter += 1

print(counter) # 16448 (+)
'''

# Task 9 - Excel
# 277 (+)

# Task 10 - Word
'''
!Без учёта регистра!
!Глава 3!
1) по
= 50 (58)
2) Вычесть
по (как отдельное слово) = 50 - 3 = 47
# (58 - 3 = 55)
3) Прибавить
по- 0
Итог = 47
# ОТВЕТ 47 -
# (55) был верным
'''

# Task 11 - paper
'''
print(2**10)
print(2**11)
print(95*11/8) # байт

print(65536*131/1024)
'''
# ANSWER = 8384 +

# Task 12
'''
max_summa = 0
for n in range(3, 10_001):
    s = '7' + '1'*n
    while '1111' in s or '7777' in s:
        if '1111' in s:
            s = s.replace('1111', '77', 1)
        else:
            s = s.replace('7777', '1', 1)
    
    cur_summa = 0
    for sym in s:
        cur_summa += int(sym)
    max_summa = max(max_summa, cur_summa)

print(max_summa) # ANSWER = 27 +
'''


# Task 13
'''
from ipaddress import ip_network

counter = 0
for ip in ip_network('192.168.32.96/255.255.255.224', strict=False):
    adr = bin(int(ip))[2:]
    if adr.count('1') % 2 == 0:
        counter += 1

print(counter) # 16 +
'''

# Task 14
'''
def dec_to_9(n):
    res = ''
    while n > 0:
        res = str(n % 9) + res
        n //= 9
    return res

num = 2*729**2019 + 2*243**2020 - 81**2021 + 2 * 27**2022 - 2 * 9**2023 - 2024

res = dec_to_9(num)
print(len(res.replace('0', ''))) # 4043 +
'''

# Task 15 - paper
# ANSWER = 23 -
# (43) был верным ответом


# Task 16
'''
def F(n):
    if n >= 2031:
        return 1
    return n + 31 + F(n + 31)

print(F(31) - F(23)) # 520 +
'''

# Task 17
'''
def is_one_from_triplet_ends5(el1, el2, el3):
    ends5_counter = 0
    if el1 % 10 == 5:
        ends5_counter += 1
    if el2 % 10 == 5:
        ends5_counter += 1
    if el3 % 10 == 5:
        ends5_counter += 1
    if ends5_counter == 1:
        return True
    return False

f = open('17.txt')
data = [int(i) for i in f]
f.close()

max_3dig_ends5 = -99999999999
for el in data:
    if el % 10 == 5 and (99 < el < 1000):
        max_3dig_ends5 = max(max_3dig_ends5, el)

triplets_counter = 0
max_triplets_sum = -99999999999


for i in range(len(data)-2):
    if is_one_from_triplet_ends5(data[i], data[i+1], data[i+2]) and sum([data[i], data[i+1], data[i+2]]) <= max_3dig_ends5:
        triplets_counter += 1
        max_triplets_sum = max(max_triplets_sum, sum([data[i], data[i+1], data[i+2]]))

print(triplets_counter, max_triplets_sum)
'''
# ANSWER: 154 861 +

# Task 18 - Excel (money labirint)
# 2353 1008 +

# Task 19 - 21 Game theory
'''
1 Куча
Ходы
+5
*3
Win S >= 135

start = range(1, 135)
'''
# s - куча
# m - ходы
"""
def F(s, m):
    if s >= 135:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [F(s+5, m-1), F(s*3, m-1)]

    return any(h) if (m-1) % 2 == 0 else all(h)

print("19)", [s for s in range(1, 135) if not F(s, 1) and F(s, 2)]) # min = 44 - (40) был верным
print("20)", [s for s in range(1, 135) if not F(s, 1) and F(s, 3)]) # 2 min: 14 35 +
print("21)", [s for s in range(1, 135) if not F(s, 2) and F(s, 4)]) # min = 30 +
"""

# Task 22 - Excel (Parallel processes)
# Ответ 14 +

# Task 23
'''
def F(x, y):
    if x > y or x == 21:
        return 0
    if x == y:
        return 1
    return F(x+1, y) + F(x*2, y) + F(x*3, y)

print(F(2, 9) * F(9, 37)) #91 +
'''

# Task 24
'''
f = open('24.txt')
line = f.readline()
f.close()
line = line.replace('FSWY', '4')
# Поиск наибольшей ручками и просмотр предшествующих и последующих символов макс. найденной последовательности\
max_seq_found = '444444444444444444444444444444444444444444444'

print(line[line.find(max_seq_found)-4:line.find(max_seq_found)+len(max_seq_found)+4])
# Максимальная найденная
# SWY444444444444444444444444444444444444444444444FSW
# 111444444444444444444444444444444444444444444444111

res = '111444444444444444444444444444444444444444444444111'
max_symbols_in_seq = 0
for el in res:
    max_symbols_in_seq += int(el)

print(max_symbols_in_seq) # ANSWER = 186 +
'''

# Task 25
'''

from fnmatch import fnmatch

for x in range(0, 10**11, 98591):
    if fnmatch(str(x), '123*45??1?'):
        print(x, x// 98591)
'''
# ANSWER: +
"""
1234457911 12521
12332452417 125087
"""

# Task 26 - excel
# 1927 77 +

# Набрал 20 первичных = 78 баллов