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


for N in range(1, 1000):
    if N % 2 == 0:
        R = bin(N)[2:] + '01'
    else:
        R = bin(N)[2:] + '10'

    dec_R = int(R, 2)
    if dec_R > 87:
        print(N)
        break

