# Task 1 - board.png
# Answer: 37

# Task 2
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ( (not (x <= y)) or ((not w) <= (not z)) or w) == 0:
                    print(x, y, z, w)
'''
# xyzw
"""
x y z w
0 0 1 0
0 1 1 0
1 1 1 0
"""

# Task 3 - Excel
# Answer: 1099

# Task 4 - Excel (draw)
# Answer: 12

# Task 5
'''
def dec_to_4(n):
    res = ''
    while n > 0:
        res = str(n % 4) + res
        n //= 4
    
    return res

for N in range(1, 10_001):
    N_4 = dec_to_4(N)
    R_4 = ''

    if N % 4 == 0:
        R_4 = N_4 + N_4[-2:]
    else:
        R_4 = N_4 + dec_to_4((N % 4) * 2)

    R = int(R_4, 4)
    if R >= 1025:
        print(N) # 66
        break
'''

# Task 6
# Сантиметры - рассмтояние между точками. ОТВЕТ: 80
'''
from turtle import *
# settings
screensize(1000, 1000)
tracer(0)
left(90)
k = 20

# movements
for i in range(3):
    pendown()
    for j in range(2):
        forward(10*k)
        right(90)
        forward(10*k)
        right(90)
    pendown()
    forward(5*k)
    right(90)
    forward(5*k)
    left(90)

# grid
penup()
for x in range(-5, 25):
    for y in range(-5, 25):
        goto(x*k, y*k)
        dot(5, 'blue')

done()
# Answer: 80
'''

# Task 7 - board
# Answer: 1600

# Task 8
'''
num = 0
counter = 0
for b1 in sorted("ФЛАМИНГО"):
    for b2 in sorted("ФЛАМИНГО"):
        for b3 in sorted("ФЛАМИНГО"):
            for b4 in sorted("ФЛАМИНГО"):
                for b5 in sorted("ФЛАМИНГО"):
                    num += 1
                    word = b1+b2+b3+b4+b5
                    if num % 2 != 0:
                        if b1 != "Н" and word.count("О") <= 1:
                            counter += 1

print(counter) # 11907
'''

# Task 9 - Excel
# Answer: 42

# Task 10 - Word
# Всего "раз" = 32
# ---
# Как отдельное слово "раз" = 7
# ===
# 32-7 = 25

# Task 11 - board
# Answer: 1365

# Task 12
'''
for n in range(3, 10_001):
    s = '4' + '1'*n

    while '31' in s or '411' in s or '1111' in s:
        if '31' in s:
            s = s.replace('31', '1', 1)
        if '411' in s:
            s = s.replace('411', '13', 1)
        if '1111' in s:
            s = s.replace('1111', '4', 1)

    res = [int(dig) for dig in s]
    if sum(res) == 36:
        print(n) #514
        break
'''

# Task 13 IP
'''
from ipaddress import ip_network

counter = 0
for ip in ip_network('23.140.159.160/255.255.252.0', False):
    adr = bin(int(ip))[2:]
    # Тут главное правильно выставить срезы для сравнения байтов числа
    if adr[:-16].count('1') >= adr[-16:].count('1'):
        counter +=1
print(counter) #176
'''

# Task 14
'''
for x in "0123456789ABCDEFGHIJKLMNO"[::-1]:
    res = int(f"1{x}2{x}3{x}4{x}5", 25) + int(f"2{x}024", 25) + int(f"1{x}099", 25)
    if res % 24 == 0:
        print(res // 24) # 11727433732
        break
'''

# Task 15
'''
for A in range(-50, 200):
    flag = True
    for x in range(0, 500):
        for y in range(0, 500):
            if ( (x < 4) or (x >= 20) or (y >= 3*x + A) or (y < 100) ) == 0:
                flag = False
                break
    if flag:
        print(A) # max A => last printed = 43
'''


# Task 16
'''
from sys import setrecursionlimit
from functools import lru_cache
setrecursionlimit(9999)

@lru_cache()
def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return n * (n-1) + F(n-1) + F(n-2)

print(F(2024) - F(2022) - 2*F(2021) - F(2020)) # 12271520
'''

# Task 17
# НЕ ЗАБЫВАЙ ИСПОЛЬЗОВАТЬ МОДУЛЬ abs()
# Для обработки отрицательных чисел!!! 
'''
def is_at_least_single_4dig(n1, n2, n3):
    n1 = abs(n1)
    n2 = abs(n2)
    n3 = abs(n3)

    counter_4dig = 0

    if 999 < n1 and n1 < 10000:
        counter_4dig += 1
    if 999 < n2 and n2 < 10000:
        counter_4dig += 1
    if 999 < n3 and n3 < 10000:
        counter_4dig += 1

    if counter_4dig >= 1:
        return True
    return False

f = open('17var03.txt')
data = [int(el) for el in f]
f.close()

max_ends_90 = 0
tripletts_counter = 0
min_triplet_sum = 99999999999

for el in data:
    if abs(el) % 100 == 90:
        max_ends_90 = max(max_ends_90, el)

counter = 0
for i in range(len(data) - 2):
    if is_at_least_single_4dig(data[i], data[i+1], data[i+2]):
        triplet_sum = (data[i] + data[i+1] + data[i+2])
        if triplet_sum > max_ends_90:
            counter += 1
            min_triplet_sum = min(min_triplet_sum, triplet_sum)

print(counter, min_triplet_sum) # 523 18038
'''

# Task 18 - Excel labirint
# --- 223

# Task 19-21 Game Theory
'''
1 Куча

Ходы:
+1
+5
*4

Победа при S >= 205
Начало 1 <= S <= 204
'''
"""
def F(s, m):
    # Победа
    if s >= 205:
        return m%2 == 0
    # Кончились ходы
    if m == 0:
        return 0
    # Все возможные ходы
    h = [F(s+1, m-1), F(s+5, m-1), F(s*4, m-1)]

    return any(h) if (m-1)%2==0 else all(h)

# Рассматриваем случаи игры при всех возможных начальных состояниях кучи и необх. условиях победы
print("19)", [s for s in range(1, 205) if not F(s, 1) and F(s, 2)]) # 51
print("20)", [s for s in range(1, 205) if not F(s, 1) and F(s, 3)]) # 2min S = 46 50
print("21)", [s for s in range(1, 205) if not F(s, 2) and F(s, 4)]) # minS = 45
"""


# Task 22 - Excel
# Answer: 19
'''
'''

# Task 23
'''
def F(x, y):
    if x > y or x == 6 or x == 17:
        return 0
    if x == y:
        return 1
    return F(x+2, y) + F(x+3, y) + F(x*5, y)

print(F(1, 31)) #  961
'''

# Task 24
# similar to task 24 var 1
'''
f = open('24var03.txt')
line = f.readline()
f.close()
A_indexes = []

for ind, el in enumerate(line):
    if el == "A":
        A_indexes.append(ind)

# print(A_indexes)

cur_seq_len = 0
min_seq_len = 10**10

for i in range(499, len(A_indexes)):
    cur_seq_len = A_indexes[i] - A_indexes[i-499]+1 # +1, чтобы получить ДЛИНУ!
    min_seq_len = min(min_seq_len, cur_seq_len)

print(min_seq_len) # 5678
'''

# Task 25
'''
from fnmatch import fnmatch

for x in range(0, 10**8+1, 5171):
    if fnmatch(str(x), '?19*8?3'):
        print(x, x//5171)
'''


# TODO: Task 26 - by Excel or Python (queue)
'''
'''
