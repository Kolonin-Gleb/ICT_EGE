# w W ц Ц
# ПОУ - программирование 
# Задание 14 - С.С.

# CLASSWORK

# 7438 % 10 = 8
# 7438 // 10 = 743
'''
x = 5 * 9**1913 + 6 * 27**2035 - 7 * 3**1721 + 10 * 81**1990 - 2023
# Записали в 3 С.С.
# Сколько значащих нулей в записи?
c = 0

while x > 0:
    if x % 3 == 0:
        c += 1
    x = x // 3
print(c)
'''

# Task 2
'''
x = 7 * 512**120 - 6 * 64**100 + 8**2100 - 255
# Записали в 18 С.С.
# Сколько значащих нулей в записи?
c = 0

while x > 0:
    if x % 18 == 0:
        c += 1
    x = x // 18
print(c)
'''

# Task 3
'''
x = 5**21 + 23**23 + 4 * 36**11 - 17**10 # В 3 С.С.
p = 1

# Найдите произведение чисел полученного числа отличных от 0
while x > 0:
    if x % 3 != 0:
        p += 1
    x = x // 3
print(p)
# 32
'''

# Задание 16 - Рекурсия
'''
def F(n):
    if n <= 1:
        return 1
    elif n % 12 == 0:
        return n + F(n - 12)
    elif n % 4 == 0:
        return n + F(n - 4)
    else:
        return 3 * F(n - 3)
print(F(51))
'''
# Задание 23 - Исполнитель
'''
'''


# HOMEWORK

# Task 1
'''
x = 123 * 456**78 + 567 * 345**21 + 89 * 123**45 - 7 * 8**9
# Записали в 7 С.С.
# Сколько 5 в записи?

c = 0

while x > 0:
    if x % 7 == 5:
        c += 1
    x = x // 7
print(c)
'''

# Task 2
'''
x = 1456**89 + 57 * 45**21 + 9 * 13**12
# Записали в 3 С.С.
# Сколько значащих 0 в записи?
c = 0

while x > 0:
    if x % 3 == 0:
        c += 1
    x = x // 3

print(c)
'''

# Task 3
'''
for x in '0123456789AB'[::-1]:
    val = int(f'1{x}A{x}', 12) - int(f'B{x}9', 12)
    if val % 6 == 0:
        print(int(x, 12))
        break
'''

# Task 4
'''
for x in '0123456789ABCD':
    val = int(f'A{x}{x}B', 14) - int(f'C0{x}', 14)
    if val % 4 == 0:
        print("val x = ", x)
        print(val / 4)
        break
'''

# Task 5 # На рекурсию
'''
def F(n):
    if n == 1:
        return 1
    return F(n - 1) * 2*n

print(F(8))
'''

# Task 6
'''
def F(n):
    if n == 1 or n == 2:
        return n
    if n > 2:
        return 2 * F(n - 1) * F(n - 2)

print(F(7))
'''

# Task 7
'''
def G(n):
    if n == 1 or n == 2:
        return 3 - n
    if n > 2:
        return G(n - 1) + F(n - 2)

def F(n):
    if n == 1 or n == 2:
        return n
    if n > 2:
        return G(n - 1) * F(n - 2) + 3

print(F(16))
'''

# Верное решение
'''
def F(n):
    if n == 1 or n == 2:
        return n
    else:
        return F(n - 1) + G(n - 2) + 3

def G(n):
    if n == 1 or n == 2:
        return 3 - n
    else:
        return G(n - 1) + F(n - 2)

result = F(16)
print(f"The value of F(16) is: {result}")
'''

# Task 8
"""
def A(n):
    if n in [0, 1, 2]:
        return n + 1
    else:
        return G(n – 1) + F(n – 1) + A(n – 1)

def F(n):
    if n in [0, 1, 2]:
        return n
    elif n > 2 and n % 2 == 0:
        return F(n - 2) + G(n – 3) + A(n – 1)
    else:
        return F(n – 1) + G(n – 2) + A(n – 3)

def G(n):
    if n in [0, 1, 2]:
        return n - 3
    elif n > 2 and n % 10 == 7:
        return 3 + G(n – 2) + F(n – 2) + A(n – 2)
    elif n > 2 and n % 10 != 7:
        return G(n – 1) + F(n – 2) + A(n – 3)

print(G(20))
"""

# ================= ВАРИАНТ ОТ CHATGPT ================= #
'''
def A(n):
    if n == 0 or n == 1 or n == 2:
        return n + 1
    else:
        return G(n - 1) + F(n - 1) + A(n - 1)

def F(n):
    if n == 0 or n == 1 or n == 2:
        return n
    elif n % 2 == 0:  # n - четное
        return F(n - 2) + G(n - 3) + A(n - 1)
    else:
        return F(n - 1) + G(n - 2) + A(n - 3)

def G(n):
    if n == 0 or n == 1 or n == 2:
        return n - 3
    elif n % 10 == 7:  # n оканчивается на 7
        return 3 + G(n - 2) + F(n - 2) + A(n - 2)
    else:
        return G(n - 1) + F(n - 2) + A(n - 3)

# Вычисляем G(20)
result_G = G(20)
print(f"The value of G(20) is: {result_G}")
'''

