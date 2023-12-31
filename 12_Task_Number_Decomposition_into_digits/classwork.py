# Task 1
# Сколько чисел в диапозоне от 437(8) до A8F(16) % 5 == 0
'''
x = int('473', 8)
y = int('A8F', 16)
k = 0
for i in range(x, y):
    if i % 5 == 0:
        k += 1

print(k) # 478
'''

# Task 2
'''
# Сумма чисел от 12345(6) до 5678(12) % 8 == 0

x = int('12345', 6)
y = int('5678', 12)
s = 0

for i in range(x, y):
    if i % 8 == 0:
        s += i

print(s) #5537112
'''

# Task 3
# Какие цифры 16 С.С. можно подставить вместо х, чтобы результат % 14 == 0
# 65x56(16) + x39x(16)
'''
for x in '0123456789ABCDEF':
    a = int('65' + x + '56', 16)
    b = int(x + '39' + x, 16)
    res = a + b
    if res % 14 == 0:
        print(x) # 0 E
'''

# Task 4
'''
# Наибольшее значение x в 12 С.С., при котором выражение % 5 == 0
for x in '0123456789AB':
    a = int(x + '413', 12)
    b = int('413' + x, 12)
    res = a + b
    if res % 5 == 0:
        print(x) 
'''

# Task 5
# При каком x значение выражения - целое число
'''
for x in '01234567':
    a = int('2A' + x + '85', 13)
    b = int('636' + x + '1', 8)
    res = a / b
    if a % b == 0: #Если числитель кратен знаменателю, то результат деления - целое число
        print(x)
'''

# Task 7
'''
for x in '01234567890AB'[::-1]:
    a = int(f"1{x}2{x}", 12)
    b = int(f"34{x}", 12)
    c = int(f"{x}", 12)

    res = a + b + c
    if res % 5 == 0: #Если числитель кратен знаменателю, то результат деления - целое число
        print(res / 5)
        break
'''

# Task 9
'''
for x in '01234567890ABCDEFJHI':
    a = int(f"{x}34{x}9", 19)
    b = int(f"1{x}814", 19)
    c = int(f"{x}", 19)

    res = a - b + c
    if res % 24 == 0:
        print(res // 24)
        break
'''






