# Исполнитель. Двоичные преобразования

# Task 1

# Набросок алгоритма:
'''
N = int(input())

bin_N = bin(N) # В 2 С.С.
bin_R = bin_N
# Добавление 2х битов чётности

for _ in 1,2:
    if bin_R[2:].count('1') % 2 == 0: # 
        bin_R += '0'
    else:
        bin_R += '1'

R = int(bin_R, base=10)
'''

# Tasks 2, 5, 6
# Укажите минимальное число R, большее, чем 140, которое могло получиться
# в результате работы этого алгоритма. 
# В ответе это число запишите в десятичной системе.
'''
# min_R = 141 # Проверяемое значение Task 2
# min_R = 43 # Проверяемое значение Task 5
# min_R = 97 # Проверяемое значение Task 6


while True:
    bin_min_R = bin(min_R)

    last_2_bits = bin_min_R[-2:] # забрать последние 2 бита чётности
    bin_min_R = bin_min_R[:-2]   # без последних 2х битов

    # Восстановление 2х битов чётности
    for _ in 1,2:
        if bin_min_R.count('1') % 2 == 0:
            bin_min_R += '0'
        else:
            bin_min_R += '1'

    if last_2_bits == bin_min_R[-2:]:
        break
    else:
        min_R += 1

print(min_R)
'''

# Tasks 2, 3, 4

'''
# Укажите минимальное число N, после обработки которого с помощью этого алгоритма получается число, большее, чем 110.
# В ответе это число запишите в десятичной системе.

# min_R = 111 # Проверяемое значение Task 2
# min_R = 137 # Проверяемое значение Task 3
# min_R = 45 # Проверяемое значение Task 4

while True:
    bin_min_R = bin(min_R)

    last_2_bits = bin_min_R[-2:] # забрать последние 2 бита чётности
    bin_min_R = bin_min_R[:-2]   # без последних 2х битов

    # Восстановление 2х битов чётности
    for _ in 1,2:
        if bin_min_R.count('1') % 2 == 0:
            bin_min_R += '0'
        else:
            bin_min_R += '1'

    if last_2_bits == bin_min_R[-2:]:
        break
    else:
        min_R += 1

print(int(bin_min_R[:-2], base=0)) # Перевод в 10 С.С.
'''

# Tasks 7
'''
max_R = 89 # Проверяемое значение Task 7

while True:
    bin_max_R = bin(max_R)

    last_2_bits = bin_max_R[-2:] # забрать последние 2 бита чётности
    bin_max_R = bin_max_R[:-2]   # без последних 2х битов

    # Восстановление 2х битов чётности
    for _ in 1,2:
        if bin_max_R.count('1') % 2 == 0:
            bin_max_R += '0'
        else:
            bin_max_R += '1'

    if last_2_bits == bin_max_R[-2:]:
        break
    else:
        max_R -= 1

print(max_R)
'''


# Task 8 Attempt 1
# Укажите минимальное число R, которое больше 102
# и может являться результатом работы данного алгоритма.
# В ответе это число запишите в десятичной системе счисления.
# Провальные попытки:
# Не 106 и Не 26
'''
# Проверяемое значение Task 8
min_N = int(input())
# Для примера
min_N = 1
# min_R = 103

while True:
    bin_min_R = bin(min_N)

    last_2_bits = bin_min_R[-2:] # забрать последние 2 бита чётности
    bin_min_R = bin_min_R[:-2]   # без последних 2х битов

    # Восстановление 2х битов
    for _ in 1,2:
        if bin_min_R.count('1') % 2 == 0:
            bin_min_R += '0'
        else:
            bin_min_R += '1'

    if last_2_bits == bin_min_R[-2:]:
        break
    else:
        min_R += 1

print(int(bin_min_R[:-2], base=0)) # Перевод в 10 С.С.
'''


# Task 8 Attempt 2
# Укажите минимальное число R, которое больше 102
# и может являться результатом работы данного алгоритма.
# В ответе это число запишите в десятичной системе счисления.
# Провальные попытки:
# Не 106 и Не 26
# ВЕРНЫЙ 105
'''
R = 0

for N in range(1, 1000):
    if N % 2 == 0:
        R = bin(N)[2:] + '01'
    else:
        R = bin(N)[2:] + '10'
    
    dec_R = int(R, 2)
    if dec_R > 102:
        print(dec_R)
        break
'''

# Task 9
'''
for N in range(1, 1000):
    if N % 2 == 0:
        R = bin(N)[2:] + '01'
    else:
        R = bin(N)[2:] + '10'

    dec_R = int(R, 2)
    if dec_R > 87:
        print(N)
        break
'''


# ========================================== CLASSORK ==========================================
# Ex 1
'''
for N in range(1, 1000):
    N_2 = bin(N)[2:]
    # Проверки на N и формирование R2
    if N_2.count('1') % 2 == 0:
        R_2 = '10' + N_2[2:] + '0' # modified N_2
    else:
        R_2 = '11' + N_2[2:] + '1' # modified N_2
    
    R = int(R_2, 2)

    if R < 42:
        print(N)
'''

# Ex 2
'''
lst = []
# m_r = 0 # Переменная контрзначение для поиска максимального R

for N in range(1, 1000):
    N_2 = bin(N)[2:]
    if N_2.count('1') % 2 == 0:
        R_2 = '11' + N_2[2:] + '00'
    else:
        R_2 = '10' + N_2[2:] + '1'
    
    R = int(R_2, 2)
    if R < 129:
        # m_r = max(m_r, R)
        lst.append(R)

print(max(lst))
# print(m_r) # Максимальное R
'''

# Ex 3
'''
for N in range(1, 1000):
    N_2 = bin(N)[2:]
    if N_2.count('1') % 2 == 0:
        R_2 = '11' + N_2[:-2] + '01'
    else:
        R_2 = '1' + N_2[:-2] + '10'

    R = int(R_2, 2)
    if R >= 380:
        print(N)
        break
'''

# Ex 4
'''
for N in range(1, 1000):
    N_2 = bin(N)[2:]
    if N_2.count('1') % 2 == 0:
        R_2 = '10' + N_2[2:] + '00'
    else:
        R_2 = '11' + N_2[2:] + '11'
    
    R = int(R_2, 2)
    if R > 229:
        if N % 2 == 0:
            print(N)
            break
'''

# Ex 5
'''
for N in range(1, 1000):
    if N % 2 == 0:
        N_2 = bin(N)[2:]
        R_2 = '1' + N_2 + '0'
    else:
        N_2 = bin(N)[2:]
        R_2 = '11' + N_2 + '11'
    R = int(R_2, 2)

    if R > 112 and R % 2 == 0:
        print(R)
        break
'''

# Ex 6
'''
for N in range(1, 1000, 2):
    N_2 = bin(N)[2:]
    R_2 = '1' + N_2[:-2] + '10'
        
    R = int(R_2, 2)

    if R < 198:
        print(N)
'''

# Ex 7
'''
for N in range(1, 1000):
    if N % 3 == 0:
        N_2 = bin(N)[2:]
        R_2 = N_2 + N_2[-3:]
    else:
        N_2 = bin(N)[2:]
        R_2 = N_2+ bin((N % 3) * 3)[2:]
    R = int(R_2, 2)

    if R >= 76:
        print(N)
        break
'''

# Ex 8 
'''
for N in range(1, 1000):
    if N % 3 == 0:
        N_2 = bin(N)[2:]
        R_2 = N_2 + N_2[-3:]
    else:
        N_2 = bin(N)[2:]
        R_2 = N_2 + bin((N % 3))[2:]
    R = int(R_2, 2)

    if R <= 40:
        print(N)
'''



# Перевод в 3 С.С.
def tr(N):
    res = ''
    
    while N / 3 > 0: # пока есть цифры
        last_dig = str(N % 3)
        N = N // 3 # осталось обработать эту часть числа
        res += last_dig

    return res[::-1]

# Ex 9 
'''
for N in range(1, 1000):
    N_3 = tr(N)
    if N % 3 == 0:
        R_3 = N_3 + N_3[-2:]
    else:
        R_3 = N_3 + tr((N % 3) * 5)

    R = int(R_3, 3)
    if R >= 86:
        print(N)
        break
'''

# Ex 10
'''
for N in range(1, 1000):
    N_3 = tr(N)
    if N % 3 == 0:
        R_3 = N_3[-2:] + N_3 + N_3[-2:]
    else:
        R_3 = tr((N % 3) * 2) + N_3

    R = int(R_3, 3)
    if R > 1000:
        print(N)
        break
'''
