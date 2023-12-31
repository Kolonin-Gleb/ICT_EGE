# Task 1
# В записи чисел переменной x обозначена неизвестная цифра из алфавита 13-ричной системы счисления.
# Определите наименьшее значение x, при котором значение данного арифметического выражения кратно 8.
# Для найденного значения x вычислите частное от деления значения арифметического выражения на 8 

'''
for x in '0123456789ABC':
    a = int(f'2023{x}', 13)
    b = int(f'100{x}{x}', 13)
    res = a + b
    # Проверка условия
    if res % 8 == 0:
        print(res // 8)
        break
'''

# Task 2
# В записи чисел переменной x обозначена неизвестная цифра из алфавита 17-ричной системы счисления.
# Определите наибольшее значение x, при котором значение данного арифметического выражения кратно 9.
# В ответ укажите значение x в десятичной системе счисления.
# Основание системы счисления в ответе указывать не нужно.
'''
for x in '0123456789ABCDEFG'[::-1]:
    a = int(f'17{x}17', 17)
    b = int(f'{x}17{x}', 17)
    res = a - b
    # Проверка условия
    if res % 9 == 0:
        print(x)
        print(int(x, 17))
        break
'''

# Task 3

'''
for x in '0123456789ABCDE':
    a = int(f'97968{x}15', 15)
    b = int(f'7{x}233', 15)
    res = a + b
    # Проверка условия
    if res % 14 == 0:
        print(res // 14)
        break
'''

# Task 4
'''
for x in '0123456789ABCDE':
    a = int(f'9897{x}21', 14)
    b = int(f'12{x}023', 14)
    res = a + b
    # Проверка условия
    if res % 13 == 0:
        print(res // 13)
        break
'''

# Task 5
'''
for x in '0123456789ABCDEF'[::-1]:
    a = int(f'99658{x}29', 16)
    b = int(f'102{x}099', 16)
    res = a + b
    # Проверка условия
    if res % 14 == 0:
        print(res // 14)
        break
'''

# Task 6
'''
for x in '0123456789ABCDEFGHI'[::-1]:
    a = int(f'98897{x}21', 19)
    b = int(f'2{x}923', 19)
    res = a + b
    if res % 18 == 0:
        print(res // 18)
        break
'''

# Task 7
'''
for x in '0123456789ABCDEFGHI':
    a = int(f'98{x}79731', 19)
    b = int(f'36{x}14', 19)
    res = a + b
    if res % 18 == 0:
        print(res // 18)
        break
'''

# Task 8
'''
for x in '0123456789ABCDEFGHI'[::-1]:
    a = int(f'139{x}822', 19)
    b = int(f'25{x}43', 19)
    c = int(f'63{x}5', 19)
    res = a + b + c
    if res % 13 == 0:
        print(int(x, 19))
        break
'''

# Task 9
'''
for x in '0123456789ABCDEFGHIJKL'[::-1]:
    a = int(f'98{x}79641', 22)
    b = int(f'36{x}14', 22)
    c = int(f'73{x}4', 22)
    res = a + b + c
    if res % 21 == 0:
        print(res // 21)
        break
'''

# Task 10
'''
'''

for x in '0123456789ABCDEFGHIJKLM'[::-1]:
    a = int(f'348{x}79643', 23)
    b = int(f'16{x}52', 23)
    c = int(f'43{x}7', 23)
    res = a + b + c
    if res % 12 == 0:
        print(int(x, 23))
        break


