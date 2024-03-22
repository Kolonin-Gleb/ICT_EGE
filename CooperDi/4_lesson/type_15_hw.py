# Задание 15
# 

# 9746
'''
for A in range(1000):
    flag = True
    for x in range(500):
        for y in range(500):
            if ( (x < A) or (y < A) or (x + 2*y > 50) ) == 0:
                flag = False
                break
    if flag:
        print(A) # 17
        break # min A is required
'''

# 9784
'''
for A in range(1000):
    flag = True
    for x in range(500):
        for y in range(500):
            if ( (x*y < A) or (x < y) or (9 < x) ) == 0:
                flag = False
                break
    if flag:
        print(A) #82
        break # min A
'''

# 10098
'''
for A in range(1000):
    flag = True
    for x in range(500):
        for y in range(500):
            if ( (x + 2*y < A) or (y > x) or (x > 60) ) == 0:
                flag = False
                break

    if flag:
        print(A) # 181
        break # min A
'''

# 12_247
'''
for A in range(1, 100_000):
    flag = True
    for x in range(1, 100_000):
        if ( (x&A == 0) or not (x&37 == 0) or not (x&12 == 0) ) == 0:
            flag = False
            break
    
    if flag:
        print(A) # 45
        # max A
'''

# TODO: Изначально взял недостаточно большие диапозоны в циклах и получил 517.
# ВЫВОД: Следует брать большие значения в циклах!!!


# 8503
'''
for A in range(10_000):
    flag = True
    for x in range(10_000):
        if (((x&52 != 0) and (x&36 == 0)) <= (x&A != 0) ) == 0:
            flag = False
            break
    
    if flag:
        print(A) # 16
        break # min A
'''

# 7594
'''
for A in range(100_000):
    flag = True
    for x in range(10_000):
        if ( (x&39 == 0) or ((x&11 != 0) or (x&A != 0)) ) == 0:
            flag = False
            break

    if flag:
        print(A) # 36
        break # min A
'''


# 7265
'''
for A in range(1, 10_000):
    flag = True
    for x in range(1, 10_000):
        if ( ((x % 2 != 0) or (x % 3 != 0)) or (x + A >= 100) ) == 0:
            flag = False
            break
    if flag:
        print(A) #94
        break # min A
'''

# 6595
'''
for A in range(1, 10_000):
    flag = True
    for x in range(1, 10_000):
        if ( ((x % 3 != 0) or (x % 2 != 0)) or (x - A >= 4) ) == 0:
            flag = False
            break
    
    if flag:
        print(A) # 2
        # max A
'''

# 4595
'''
for A in range(1, 10_000):
    flag = True
    for x in range(1, 10_000):
        if ( ((x % 2 != 0) or (x % 3 != 0)) or (x + A >= 80) ) == 0:
            flag = False
            break

    if flag:
        print(A) # 74
        break # min A
'''

# 746
# Подсмотрел как решать с импликацией и решил в тетради
# https://www.youtube.com/watch?v=VCL7rhHZRq4
# TODO: Почему рассматривается два случая при импликации, а именно когда:
# P = 1 Q = 0
# P = 0 Q = 1
# Хочется разобраться подробнее

# 1198
# TODO: Не понимаю.
# https://www.youtube.com/watch?v=vT8H1vsifTo
'''
'''

# 1276
# Ответ 18. Решение в тетради
'''
'''

# 1440
# TODO: Не знаю, как решить. Как сделать на бумаге?
'''
'''

# 754
# Работа с множествами
# TODO: Также не понимаю момент с импликацией и упрощением функции.
'''
'''
#  P = {2,  4,  6,  8, 10, 12, 14, 16, 18, 20}
# Q  = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
# res = {2, 4, 6, 8, 12, 14, 16, 18}
# количество = 8
# Ответ: 8

# 1072
# Решил сам опираясь на разборы предыдущих
'''
'''
# P   = {2, 4, 6,  8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30}
# Q   = {1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31}
# res = {2 6 8 12 14 18 20 24 26 30   }
# Количество = 10


# 1409
# Справился сам
'''
'''
# Edited sets
# P = {2,   4,  6,  8, 10, , 14, 16, 18, 20}
# Q = {3,   6,  9, , 15, 18, 21, , 27, 30}
# R = {12, 24, 36, 48, 60}
# res = 6 18 
# Произведение = 108
