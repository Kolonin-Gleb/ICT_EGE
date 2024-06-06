# TODO: Task 1 - board.png
# Answer: 32

# Task 2
# Сложная варианция с F = 1 and F = 0 at the same time
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ( x and (y <= z) and ( (not y) <= ( (not z) == w )) ) == 1:
                    print(x, y, z, w)
'''
# 
"""
"""

# Task 3 - Excel
# Answer: 1453717

# Task 4 - Excel (draw)
# Answer: 18

# Task 5
'''
for N in range(1, 10_001):
    N_2 = bin(N)[2:]
    R_2 = ''

    if N % 2 == 0:
        R_2 = N_2 + '0'
    else:
        R_2 = N_2 + '1'
    
    if R_2.count('1') % 3 == 0:
        R_2 = '11' + R_2[2:]
    else:
        R_2 = '10' + R_2[2:]

    R = int(R_2, 2)

    if R >= 26:
        print(N) # 9
        break
'''


# Task 6
# TODO: Разобрать с Димой. Слишком большая фигура
# Тут решили с использованием canvas:
# https://youtu.be/hXSa3GPJems?si=2L0sksko69sciuB8&t=1944
'''
from turtle import *
# settings
screensize(1_000, 10_000)
tracer(0)
left(90)
k = 20

# movement
forward(100*k)
right(90)
forward(100*k)
right(30)
pendown()
for i in range(10):
    forward(25*k)
    right(90)

# grid
penup()
for x in range(-20, 20):
    for y in range(-20, 100):
        goto(x*k, y*k)
        dot(5, 'blue')

done()
'''

# Task 7 - board
# Answer: 4

# Task 8
'''
counter = 0
for d1 in '1234567':
    for d2 in '01234567':
        for d3 in '01234567':
            for d4 in '01234567':
                for d5 in '01234567':
                    num = d1+d2+d3+d4+d5
                    if num.count('4') == 2:
                        if '14' not in num and '34' not in num and '54' not in num and '74' not in num:
                            if '41' not in num and '43' not in num and '45' not in num and '47' not in num:
                                counter += 1

print(counter) #612
'''

# Task 9 - Excel
# Answer: 1


# Task 10 - Word
# Answer: 6

# Task 11 - board
# Answer: 2800

# Task 12
'''
s = '22' + '1'*2023 + '22'

while '211' in s or '112' in s:
    s = s.replace('11', '1', 1)
    if '21' in s:
        s = s.replace('21', '12', 1)
    else:
        s = s.replace('12', '1', 1)

print(s) # 121222
'''

# Task 13 IP
'''
from ipaddress import ip_network

counter = 0
for ip in ip_network('252.67.33.87/255.252.0.0', False):
    adr = bin(int(ip))[2:]
    byte_1_and_2 = adr[:-16]
    byte_3_and_4 = adr[-16:]

    # Быть крайне внимательным при записи условий!!!
    if byte_1_and_2.count('1')*2 < byte_3_and_4.count('1'):
        counter += 1
    
print(counter) #17
'''

# Task 14
'''
def dec_to_5(num):
    res = ''
    while num > 0:
        res = str(num % 5) + res
        num //= 5
    
    return res

num = 4 * 25**2022 - 2 * 5**2000 + 125**1011 - 3*5**100 - 660

num_5 = dec_to_5(num)
print(num_5.count('4')) # 3028
'''

# Task 15
'''
for A in range(1, 1_001):
    flag = True
    for x in range(1, 501):
        if ( ((x % 13 == 0) <= (x % 21 != 0)) or (x + A >= 500)) == 0:
            flag = False
            break
    if flag:
        print(A) # 227
        break # min A required
'''

# Task 16
'''
def F(n):
    if n < 3:
        return n
    if n > 2 and n%2 == 0:
        return (2*(n-1) + F(n-1) + 2)
    if n > 2 and n%2 != 0:
        return (2*(n+1) + F(n-2) - 5)
print(F(32)) #530
'''

# Task 17
'''
f = open('17var05.txt')
data = [int(el) for el in f]
f.close()

max_el = max(data)
pair_counter = 0

max_sum_of_squares = 0

for i in range(len(data)-1):
    if data[i] + data[i+1] == max_el:
        pair_counter += 1
        max_sum_of_squares = max(max_sum_of_squares, (data[i]**2 + data[i+1]**2))

print(pair_counter, max_sum_of_squares) # 2 9997800125
'''

# Task 18 - Excel labirint
# Answer: 1174 598

# Task 19-21 Game Theory
'''
1 Куча

Ходы:
+1
*2

Победа при S >= 229
Начало 1 <= S <= 228
'''
"""
def F(s, m):
    if s >= 229:
        return m%2 == 0
    if m == 0:
        return 0
    
    h = [F(s+1,m-1), F(s*2, m-1)]

    return any(h) if (m-1)%2 == 0  else all(h)


print("19)", [s for s in range(1, 229) if not F(s, 1) and F(s, 2)]) # 114
print("20)", [s for s in range(1, 229) if not F(s, 1) and F(s, 3)]) # 2min S = 57 113
print("21)", [s for s in range(1, 229) if not F(s, 2) and F(s, 4)]) # 112 
"""

# Task 22 - Excel
# Answer: 17

# Task 23
'''
def F(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    return F(x-1, y) + F(x//2, y)

print(F(50, 20) * F(20, 1)) # 2340
'''

# Task 24
'''
f = open('24var05.txt')
line = f.readline()
f.close()

# Список индексов A
A_indexes = []
for i in range(len(line)):
    if line[i] == "A":
        A_indexes.append(i)

max_seq_len = 0
# Проходим по списку индексов А
for i in range(len(A_indexes) - 4):
    # Найдём индексы начала и конца каждой последовательности содержащей 3 А
    start_index = A_indexes[i] + 1
    end_index = A_indexes[i + 4] - 1

    cur_seq_len = end_index - start_index + 1 # +1, т.к. длина на 1 больше разницы индексов

    max_seq_len = max(max_seq_len, cur_seq_len)

print(max_seq_len) #501
'''

# Task 25
'''
from fnmatch import fnmatch

for x in range(0, 10**8, 149):
    if fnmatch(str(x), '11*223'):
        print(x, x//149)
'''

# TODO: Task 26 - by Excel or Python (queue)
'''
'''
