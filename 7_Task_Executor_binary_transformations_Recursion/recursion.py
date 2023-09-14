# Функция вычисления НОД - Наибольший общий делитель
'''
def NOD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    print(a + b)

NOD(18, 30) # 6
'''

# Пример 16 задания ЕГЭ
# Алгоритм вычисления значения функции F(n)
# F(n) = 3, при n = 1
# F(n) = 3 - n + F(n - 1), при n % 2 == 0
# F(n) = 3 * F(n - 2), при n > 1 and n % 2 == 1
# F(18) = ?
'''

def F(n):
    if n == 1: # Базовое условие
        return 3
    elif n % 2 == 0:
        return 3 - n + F(n - 1)
    elif n % 2 == 1:
        return 3 * F(n - 2)

print(F(18)) # 19668
'''

# Task 2
'''
def f(a, b):
    print(a*b/2, a+b+(a**2 + b**2)**0.5)
f(3, 4)
'''

# Task 3
'''
def F(n):
    if n == 1:
        return 3
    elif n > 1:
        return F(n-1) + 2 * n
print(F(31))
'''

# Task 4
'''
def F(n):
    if n == 1 or n == 2:
        return n
    elif n > 2:
        return F(n - 1) + F(n - 2)

print(F(17))
'''

# Task 5
'''
def F(n):
    if n == 1:
        return 2
    elif n > 1:
        return F(n - 1) + 3 * n

print(F(38))
'''

# Task 6
'''
def F(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 2 * F(n - 1)
    elif n % 2 == 1:
        return F(n - 2) + 3
print(F(46))
'''

# Task 7
'''
def F(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + F(n-1)
    if n % 2 == 1:
        return 2 * F(n - 1)
print(F(19))
'''

# Task 8
'''
def F(n):
    if n == 1 or n == 2 or n == 3:
        return n
    elif n > 3:
        return F(n - 3) + F(n - 2)

print(F(21))
'''

# Task (9) 10
'''
def F(n):
    if n == 1 or n == 2:
        return n
    if n > 2:
        return F(n - 1) + 2 * G(n - 2)

def G(n):
    if n == 1 or n == 2:
        return n
    if n > 2:
        return 2 * G(n - 1) + F(n - 2)

print(F(12))
'''

import sys

sys.setrecursionlimit(10000)
'''
def F(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * F(n - 1)

a = F(2041)
b = F(2038)
print(a / b)
'''

'''
def F(n):
    if n == 0:
        return 1
    elif n > 0:
        return 4 * F(n - 1)

a = F(3050)
b = F(3040)
print(a / b)
'''

'''
def G(n):
    if n >= 1024:
        return n
    else:
        return G(n + 2) + n

a = G(1012)
b = G(1021)
print(a - b)
'''

'''
def G(n):
    if n < 5172:
        return 2 * n + G(n + 2)
    else:
        return 3 * n

print(G(5120) - G(5130) + G(5110))
'''
