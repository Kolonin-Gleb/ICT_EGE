# Разбор решений 15 задания из ЕГЭ
# Шаблон
"""
for A in range(1, 500): # Если А - натуральное число, то диапозон начинается с 1
    flag = True # Флаг показывающий, подходит ли нам параметр
    for x in range(1, 500): # Если в задании речь о натуральных числах, то с 1
        for y in range(1, 500): # кол. циклов = кол. переменных в задании
            if "Выражение из условия" == 0:    # 
                flag = False # Состояние флага - параметр не подошёл
                break # Дальше нет смысла проверять
    if flag == True:  # Найден ответ
        print(A)      # Вывод  ответа
"""

# This soultion doesn't work!
# Task 1
"""
for A in range(10_000): # А - целое неотрицательное число => диапозон начинается с 0
    flag = True # Флаг показывающий, подходит ли нам параметр
    for x in range(500): # В задании речь о целых неотрицательных числах, то с 1
        for y in range(500): # кол. циклов = кол. переменных в задании
            if ((2*x + y < 40) or (x + y >= A)) == 0:
                flag = False # Состояние флага - параметр не подошёл
                break # Дальше нет смысла проверять
    if flag == True:  # Найден ответ
        print(A)      # Вывод  ответа
"""

# Task 1 ChatGPT solution - working
'''
def find_largest_A():
    largest_A = 0
    for A in range(100):  # Предполагаем, что A не превысит 100 (можно увеличить, если необходимо)
        found = True
        for x in range(100):  # Предполагаем, что x не превысит 100 (можно увеличить, если необходимо)
            for y in range(100):  # Предполагаем, что y не превысит 100 (можно увеличить, если необходимо)
                if not ((2 * x + y < 40) or (x + y >= A)):
                    found = False
                    break
            if not found:
                break
        if found:
            largest_A = A

    return largest_A

result = find_largest_A()
print("Наибольшее значение A:", result)
'''

# Task 2
'''
for A in range(10_000): # A - целое неотр. число
    if A % 100 == 0:
        print(f"progress = {A}")

    flag = True
    for x in range(500):
        for y in range(500):
            if ((x&47 != 0) <= ((x&11 == 0) <= (x&A != 0))) == 0: # Следует либо упростить формулу, либо расставить ()
                flag = False # Параметр не подошёл
                break
    if flag == True:
        print(A)
        break # Т.к. просят найти наименьшее
'''

# Task 3
'''
for A in range(1000):
    flag = True
    for x in range(500):
        for y in range(500):
            if ((3*y + 7*x < A) or (x > 48) or (y > 32)) == 0:
                flag = False
                break
    if flag == True:
        print(A)
        break # т.к. просят найти наименьшее
'''

# Task 4
'''
for A in range(1, 1000):
    if A % 100 == 0:
        print(f"progress = {A}")
    flag = True
    for x in range(1, 500):
        for y in range(1, 500):
            if ( (x % 7 == 0) <= ((A + 3*x < 333) <= (x % 3 != 0)) ) == 0:
                flag = False
                break
    if flag == True:
        print(A)
        break # т.к. просят найти наименьшее
'''

# Task 5
'''
P = [45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]

for A in range(1, 1000):
    if A % 100 == 0:
        print(f"progress = {A}")
    flag = True
    for x in range(1, 1000):
        if ((x % A == 0) or ((x in P) <= (x % 8 != 0))) == 0:
            flag = False
            break
    if flag == True:
        print(A) # Нужно наибольшее
'''

# Task 6
'''
P = list(range(50, 71))

for A in range(1, 1000):
    if A % 100 == 0:
        print(f"progress = {A}")
    flag = True
    for x in range(1, 1000):
        if (not(x in P) or ((x % 11 == 0) == (not(x in P))) or (50 + x < A)) == 0:
            flag = False
            break
    if flag == True:
        print(A)
        break # Т.к. нужно наименьшее
'''

# Task 7
'''
for A in range(1000):
    flag = True
    for x in range(1000):
        for y in range(1000):
            if ( (99 != (y + 2*x) ) or (A < x) or (A < y)) == 0:
                flag = False
                break
    if flag:
        print(A)
        # Нужно наибольшее
'''

# Task 8
'''
for A in range(1000):
    flag = True
    for x in range(1000):
        if ( ((x&52 != 0) and (x&36 == 0)) <= (not(x&A == 0))) == 0:
            flag = False
            break
    if flag:
        print(A)
        break # Т.к. наименьшего!
'''

# Task 9
'''
for A in range(1, 1000):
    flag = True
    for x in range(1000):
        if ( ((x % A != 0) and (x % 24 == 0)) <= ((x % 16 != 0)  or ((x % 24 != 0))) ) == 0:
            flag = False
            break
    if flag:
        print(A) # Нужно наибольшее
'''

# Task 10
'''
for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if ( (x % 3 == 0) <= (x % 5 != 0) or (x+A >= 90)) == 0:
            flag = False
            break
    if flag:
        print(A)
        break
'''

