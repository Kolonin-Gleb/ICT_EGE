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

# TODO: Task 3 - Excel

# TODO: Task 4 - Excel (draw + table)

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

# Task 7 - board/paper

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

# Task 9 - Excel

# Task 10 - Word

# Task 11 - board/paper

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

# TODO: Позже. Task 14
'''
'''


# Task 15
'''
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
'''

# Task 18 - Excel labirint

# Task 19-21 Game Theory
# TODO: Разобрать с Димой!!
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

    return any(h) if (m-1 % 2) == 0 else all(h) # Для неудачного заменить 2th all to any

# Петя не выиграет 1ым ходом, но Ваня побеждает своим 1ым ходом
print("19)", [s for s in range(1, 202) if not F(s, 1) and F(s, 2)]) # 67
print("20)", [s for s in range(1, 202) if not F(s, 1) and F(s, 3)]) # 
print("21)", [s for s in range(1, 202) if not F(s, 2) and F(s, 4) or F(s, 6)]) # 
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
'''
'''



# Task 25
# TODO: Ответ не сходится!
'''
from fnmatch import fnmatch
# В этом номере начинаем цикл с 0, не смотря на натуральные числа
for i in range(0, 10**10, 31007):
    if fnmatch(str(i), '123*4?5'):
        print(i, i//31007)
'''

# Task 26 - ??


