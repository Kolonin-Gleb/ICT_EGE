# Task 1 - board.png
# Answer: 34

# Task 2
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ( (not (x <= y)) or (x == z) or w ) == 0:
                    print(x, y, z, w)
'''
# xwzy

# Task 5
'''
def dec_to_4(n):
    res=''
    while n > 0:
        res = str(n % 4) + res
        n//=4
    return res

for N in range(1, 10_001):
    N_4 = dec_to_4(N)
    R_4 = ''

    if N % 4 == 0:
        R_4 = N_4 + N_4[-2:]
    else:
        R_4 = N_4 + dec_to_4((N % 4) * 2)

    R = int(R_4, 4)    
    if R < 261:
        print(N) # Нужно максимальное
'''
# Answer: 61

# Task 6
'''
from turtle import *
# Settings
screensize(1000, 3000)
tracer(0)
left(90)
k = 2

# Movement
for i in range(2):
    forward(17*k)
    left(90)
    forward(10*k)
    left(90)

penup()
backward(4*k)
right(90)
backward(3*k)
left(90)
pendown()

for i in range(2):
    forward(40*k)
    right(90)
    forward(10*k)
    right(90)

# Grid
penup()

for x in range(-10, 20):
    for y in range(-10, 50):
        goto(x*k, y*k)
        dot(4, 'blue')

done()
'''
#577

# Task 8
'''
counter = 0
num = 0
for b1 in sorted("ФАВОРИТ"):
    for b2 in sorted("ФАВОРИТ"):
        for b3 in sorted("ФАВОРИТ"):
            for b4 in sorted("ФАВОРИТ"):
                for b5 in sorted("ФАВОРИТ"):
                    for b6 in sorted("ФАВОРИТ"):
                        num +=1
                        word = b1+b2+b3+b4+b5+b6
                        if num % 2 == 0 and b1 != 'О' and word.count("Р") == 2:
                            counter += 1
print(counter) #8640
'''

# Task 12
'''
for n in range(3, 10_001):
    s = '1' + '2'*n

    while '12' in s or '3322' in s or '2222' in  s:
        if '12' in s:
            s = s.replace('12', '33', 1)
        if '2222' in s:
            s = s.replace('2222', '1', 1)
        if '3322' in s:
            s = s.replace('3322', '21', 1)

    summa = 0
    for dig in s:
        summa += int(dig)
    if summa == 218:
        print(n) #177
        break
'''

# Task 13 IP
# Посмотрел видеоразбор:
# https://youtu.be/KI0-mSxPAvo?si=RB3EemLAY-1NWUUr&t=2786
'''
from ipaddress import ip_network
# В функцию ip_network подать: адрес_сети/маска_сети

net = ip_network("142.108.56.118/255.255.255.240", strict=False)

counter = 0
for ip in net:
    # Переводим ip адрес в двоичный вид
    adr = bin(int(ip))[2:]

    # кол. ед. в левых 2х байтах меньше кол. ед. в правых 2х байтах
    if adr[:-16].count('1') < adr[-16:].count('1'):
        counter += 1
    
print(counter) # 5
'''

# Task 14
# Новый подход
'''
for x in "0123456789ABCDEFGHIJKLM":
    num1 = int(f"1{x}1{x}1{x}1{x}1", 23)
    num2 = int(f"20{x}24", 23)
    num3 = int(f"1{x}235", 23)
    res = num1+num2+num3
    if res % 22 == 0:
        print(res // 22) # 4651779499
        break
'''

# Task 15
'''
for A in range(-1000, 1000):
    flag = True
    for x in range(0, 300):
        for y in range(0, 300):
            if ((4*x + y < A) or (x < y) or (22 <= x)) == 0:
                flag = False
                break
    if flag:
        print(A) # 106
        break
'''


# Task 16
'''
from sys import setrecursionlimit
setrecursionlimit(9999)

def F(n):
    if n == 1:
        return 5
    return 2*n + 1 + F(n - 1)

print(F(2024) - F(2022)) #8096
'''

# Task 17
'''
def is_single_2dig_num(n1, n2, n3):
    counter_2dig_num = 0
    if n1 > 9 and n1 < 100:
        counter_2dig_num += 1
    if n2 > 9 and n2 < 100:
        counter_2dig_num += 1
    if n3 > 9 and n3 < 100:
        counter_2dig_num += 1

    if counter_2dig_num == 1:
        return True
    return False

f = open('17var01.txt')
data = [int(el) for el in f]
f.close()

triplets_counter = 0
max_triplet_sum = 0

min_ends_25 = 999999999925

for el in data:
    if el % 100 == 25:
        min_ends_25 = min(min_ends_25, el)

for i in range(len(data)-2):
    if is_single_2dig_num(data[i], data[i+1], data[i+2]):
        triplet_sum = (data[i] + data[i+1] + data[i+2])
        if triplet_sum < min_ends_25:
            max_triplet_sum = max(max_triplet_sum, triplet_sum)
            triplets_counter += 1
        
print(triplets_counter, max_triplet_sum) # 247 41
'''

# Task 18 - Excel labirint

# Task 19-21 Game Theory
# Вспоминаю, разбираюсь, повторяю
'''
Ходы:
+1
+4
*3
Победа при S >= 202
Начало 1 <= S <= 201
'''
"""
def F(s, m):
    # Победа одного из игроков
    if s >= 202:
        return m % 2 == 0
    # Ходы израсходованы
    if m == 0:
        return 0
    # Рассмотреть все возможные ходы
    h = [F(s+1, m-1), F(s+4, m-1), F(s*3, m-1)]
    # (m-1) - обязательно в скобках. Задаёт приоритет!
    return any(h) if (m-1) % 2 == 0 else all(h) # Для неудачного заменить 2th all to any

# Петя не выиграет 1ым ходом, но Ваня побеждает своим 1ым ходом
print("19)", [s for s in range(1, 202) if not F(s, 1) and F(s, 2)]) # 67
print("20)", [s for s in range(1, 202) if not F(s, 1) and F(s, 3)]) # 63 66
print("21)", [s for s in range(1, 202) if not F(s, 2) and F(s, 4)]) # min 62
"""


# Task 22 - Excel

# Task 23
'''
def F(x, y):
    if x > y or x == 11 or x == 17:
        return 0
    if x == y:
        return 1
    return F(x+1, y) + F(x+4, y) + F(x*2, y)

print(F(3, 24)) #298
'''

# Task 24
# index - место где встречается
# Сколько раз встретилось А
# Работая с index-ами определить мин. разницу
'''
f = open('24var01.txt')
line = f.readline()
f.close()
A_indexes = []

for ind, el in enumerate(line):
    if el == "A":
        A_indexes.append(ind)

# print(A_indexes)

cur_seq_len = 0
min_seq_len = 10**10

for i in range(2023, len(A_indexes)):
    cur_seq_len = A_indexes[i] - A_indexes[i-2023]+1 # +1, чтобы получить ДЛИНУ!
    min_seq_len = min(min_seq_len, cur_seq_len)

print(min_seq_len) #7001
'''

# Task 25
'''
from fnmatch import fnmatch
# В этом номере начинаем цикл с 0, не смотря на натуральные числа
for i in range(0, 10**10, 31007):
    if fnmatch(str(i), '1*34?5?9'):
        print(i, i//31007)
'''

# Task 26 - by Python (queue)
'''
f = open('26var01.txt')
f.readline()
data = []

for el in f:
    st, duration = map(int, el.split())
    data.append([st+duration, st])

# print(data[:10])
data.sort()
# print(data[:10])

attended = [] # Посещенные встречи
cur_time = 0 # в минутах (время освобождения CEO)

potential_26 = []

for el in data:
    # Потенциальные 26 встречи
    if len(attended) == 25 and el[1] >= cur_time: # Рассматриваемая встреча может быть посещена
        potential_26.append(el)

    elif len(attended) != 25 and el[1] >= cur_time: # Время старта > время окончания тек. встречи (освобождения CEO)
        attended.append(el)
        cur_time = el[0]

print(attended[-1][0]) # Время окончания 25 встречи
print(potential_26) # Глазами увидили, что макс. перерыв = 20

print(len(attended)) # Сколько встреч сможем посетим = 26
f.close()
'''
