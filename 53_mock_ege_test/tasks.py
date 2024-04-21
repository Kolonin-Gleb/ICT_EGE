# Task 2
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ( (x or (not y)) and (y == (not z)) and w ) == 1:
                    print(x, y, z, w)
'''
# wxyz
'''
x y z w
0 0 1 1
1 0 1 1
1 1 0 1
'''

# Task 10 Notes
'''
С помощью текстового редактора определите, сколько раз, НЕ СЧИТАЯ СНОСОК, встречаются слова
«сударь» (или «Сударь») и 
17 раз
«сударыня» (или «Сударыня») в тексте комедии А.С. Грибоедова «Горе от ума».
8 раз
Другие формы слов (такие как «сударю», «сударя» и т.д.) учитывать не следует.

В ответе укажите только число: 17 + 8 = 25
'''

# Task 5
'''

for N in range(10_000):
    N_2 = bin(N)[2:]

    if N % 2 == 0:
        R_2 = N_2 + '11'
    else:
        R_2 = "1" + N_2 + "01"

    R = int(R_2, 2)
    if R < 711:
        print(N)
        # 176 - max
'''

# Task 6
# Turtle
"""
from turtle import *
# Настройка
screensize(10_000, 10_000)
tracer(0)
left(90)
k = 40

# Перемещения
for i in range(2):
    forward(20*k)
    right(90)
    forward(10*k)
    right(90)

penup()

forward(4*k)
right(90)
forward(5*k)
left(90)

pendown()

for i in range(2):
    forward(5*k)
    right(90)
    forward(30*k)
    right(90)

penup()
# Сетка
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x*k, y*k)
        dot(5, 'blue')

# В пересечении 36 точек
done()
"""

# Task 7
'''
i = (23*1024*1024*8)//(5560*2560)
print(i)
print(2**i) # K
'''

# Task 8
'''
num = 0
for b1 in sorted("ЕЛКА"):
    for b2 in sorted("ЕЛКА"):
        for b3 in sorted("ЕЛКА"):
            for b4 in sorted("ЕЛКА"):
                for b5 in sorted("ЕЛКА"):
                    num += 1
                    word = b1+b2+b3+b4+b5
                    # print(num, word)
                    # exit()
                    if word.count("А") <= 1 and word.count('К') == 2 and word.count("Л") == 0:
                        print(num, word) #91
                        break
'''

# Task 12 #TODO: ПОЧЕМУ НЕТ ВЫВОДА?
'''
def is_prime(n):
    flag = True
    for i in range(2, n//2+1):
        if n % i != 0:
            flag = False
            break
    return flag


for n in range(10_000):
    s = ">" + '3'*15 + '4'*n + '5'*19

    while '>3' in s or '>4' in s or '>5' in s:
        if ">3" in s:
            s = s.replace('>3', '1>', 1)
        elif ">4" in s:
            s = s.replace('>4', '2>', 1)
        elif ">5" in s:
            s = s.replace('>5', '31>', 1)
    
    summa = 0
    for el in s[:-1]:
        summa += int(el)
    
    # print(summa)

    if is_prime(summa):
        print(n) # minimal N
        break
'''

# Task 13
'''
# net  = '178.054.080.0'
print(bin(80)[2:].zfill(8))
# mask = '255.255.240.0'
print(bin(240)[2:].zfill(8))


# 11111111.11111111.01010000.00000000 # net 
# 11111111.11111111.11110000.00000000 # mask
# 11111111.11111111.01010000.00000000 # ip
'''
# Павильно ли я определил ip?
# Что делать дальше?

# Task 14
'''
def dec_to_4(n):
    res = ''
    while n > 0:
        res = str(n % 4) + res
        n //= 4
    return res

num = 100**2023 + 23 * 10**23 + 20**23 + 101

# 4321
print(dec_to_4(num).count('0') + dec_to_4(num).count('3'))
'''

# Task 15
'''
B = list(range(20, 56))

for A in range(10_000):
    flag = True
    for x in range(1000):
        if ( (x % 3 == 0) or ((x in B) <= (2*x + A >= 74)) ) != 1: # Условие нарушено
            flag = False
    if flag:
        print(A) # 34
        break
'''

# Task 16
'''
import sys
sys.setrecursionlimit(9999)

def F(n):
    if n <= 2000:
        return 1
    return 4 * F(n - 1) 

print(F(2300) // F(2290)) # 1048576
'''

# Task 23
'''
def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 1, y) + f(x + 2, y) + f(x * 2, y)

print(f(3, 9) * f(9, 11) * f(11, 15)) # 170
'''

# Task 24
'''
glasniy = 'AE' # 1
soglasniy = 'BCD' # 0

f = open('24.txt')
line = f.readline().replace('A', '1').replace('E', '1')
line = line.replace('B', '0').replace('C', '0').replace('D', '0')
f.close()

print(line)

k = 1 # лок. макс
m = 1 # глоб. макс

for i in range(0, len(line) - 1, 2):
    if line[i] == '1' and line[i+1] == '0':
        k += 1
    else:
        m = max(k, m)
        k = 1

print(m) # 9 пар
'''

# Task 25
'''
from fnmatch import fnmatch

for x in range(0, 10**8, 197):
    if fnmatch(str(x), '70?53*1?'):
        print(x, x // 197)
'''

# Task 19
'''
2 Кучи

Ходы:
+1
*2
a = 12
b = [1;61]
Победа при a + b = S >= 74 
'''
"""
def F(a, b, m):
    # усл. победы
    if a + b >= 74:
        return m%2 == 0
    if m == 0: # ходы кончились
        return 0
    # Все варианты ходов
    h = [F(a+1, b, m-1), F(a*2, b, m-1), F(a, b+1, m-1), F(a, b*2, m-1)]
    # Заученная формула
    return any(h) if (m-1) % 2 == 0 else all(h) # any для неудачного хода

# В циклах перебирается кача b и делается проверка на интересующий нас исход партии
print("19) ", [b for b in range(1, 62) if F(12, b, 2)]) # min = 16
print("20) ", [b for b in range(1, 62) if not F(12, b, 1) and F(12, b, 3)]) # 2430
print("21) ", [b for b in range(1, 62) if not F(12, b, 2) and F(12, b, 4)]) # 29
"""

# Task 17
'''
'''

f = open("17.txt")



f.close()

