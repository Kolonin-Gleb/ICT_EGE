# Task 1
'''
def f(bin_n):
    summa = 0
    for i in range(len(bin_n)):
        summa += int(bin_n[i]) # 
    return summa

for n in range(1, 100):
    bin_n = bin(n)[2:] # перевод в двоичную систему
    summa = f(bin_n) # Рассчёт суммы
    bin_n = bin_n + str(summa % 2) # Дописать остаток к числу

    # Повтор операции с новым числом
    summa = f(bin_n)
    bin_r = bin_n + str(summa % 2)


    r = int(bin_r, 2) # перевод в десятичную систему
    if r > 78:
        print(r)
        break
'''

# Task 2
'''
# Функция для суммирования цифр числа в 2 С.С.
def F(bin_n):
    summa = 0
    for i in range(len(bin_n)):
        summa += int(bin_n[i])
    return summa

for n in range(1, 100):
    bin_n = bin(n)[2:]
    summa = F(bin_n)
    bin_n += str(summa % 2) # Добавление остатка к числу

    # Повтор операции с новым числом
    summa = F(bin_n)
    bin_r = bin_n + str(summa % 2)

    r = int(bin_r, 2)
    if r > 49:
        print(n)
        break
'''

# Task 3
'''
for n in range(1, 10000):
    bin_n = bin(n)[2:]
    bin_n += str(bin_n.count('1') % 2)

    bin_r = bin_n + str(bin_n.count('1') % 2)

    r = int(bin_r, 2)

    if r > 396:
        print(r)
        break
'''

# Task 4
'''
for n in range(1, 10000):
    bin_n = bin(n)[2:]
    bin_n += str(bin_n.count('1') % 2)

    bin_r = bin_n + str(bin_n.count('1') % 2)
    r = int(bin_r, 2)

    if r > 445:
        print(n)
        break
'''

# Task 5
'''
for n in range(1, 10000):
    bin_n = bin(n)[2:]
    if bin_n.count('1') % 2 == 0:
        bin_n += '0'
        bin_n = '10' + bin_n[2:]
    else:
        bin_n += '1'
        bin_n = '11' + bin_n[2:]

    r = int(bin_n, 2)

    if r > 190:
        print(r)
        break
'''

# Task 6
'''
а) если сумма цифр в двоичной записи числа чётная, то к этой записи справа дописывается 1, 
а затем два левых разряда заменяются на 11;
# ####################################################################################### #
б) если сумма цифр в двоичной записи числа нечётная, то к этой записи справа дописывается 0, 
а затем два левых разряда заменяются на 10.
'''

# Укажите такое наибольшее число N, для которого результат работы алгоритма меньше 35.
'''
for n in range(1, 10000):
    bin_n = bin(n)[2:]
    if bin_n.count('1') == 0:
        bin_n = '11' + bin_n[2:] + '1'
    else:
        bin_n = '10' + bin_n[2:] + '0'

    r = int(bin_n, 2)

    if r < 35:
        print(n)
'''

# Task 7
'''
for n in range(1, 1000):
    bin_n = bin(n)[2:]

    if bin_n.count('1') % 2 == 0:
        bin_n = bin_n + '00'
    else:
        bin_n = bin_n + '11'
    
    r = int(bin_n, 2)

    if r > 99:
        print(r)
        break
'''

# Task 8
'''
x = 0
y = 0

x += 15
y += 15
for i in range(7):
    x -= 5
    y += 10

    x += 10
    y -= 5

y += 3

# Позиция
print(x, y)
# Суммарное смещение, чтобы вернуться в 0, 0
print(-x-y)
'''

# Task 9
# n = НОД(16, 4) = 4

# Task 10
'''
'''

# Task 11
'''
'''

