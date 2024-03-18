# ПОУ. Алгоритмизация 2

# Task 1
'''
for N in range(1, 100):
    N_2 = bin(N)[2:]

    R = N_2 + str(N_2.count('1') % 2)
    R = R + str(R.count('1') % 2)

    if int(R, 2) > 78:
        print(int(R, 2)) # 80
        break
'''

# Task 2
'''
for N in range(1, 100):
    N_2 = bin(N)[2:]

    if N_2.count('1') % 2 == 0:
        R = '10' + N_2 + '01'
    else:
        R = '1' + N_2 + '10'

    if int(R, 2) <= 66:
        print(N) # max = 7
'''

# Task 3
'''
for N in range(1, 100):
    N_2 = bin(N)[2:]
    if N_2.count('1') % 2 == 0:
        R = '10' + N_2 + '01'
    else:
        R = '1' + N_2 + '11'
    
    if int(R, 2) > 146:
        print(N)
        break
'''

# Task 4
'''
for N in range(1, 100):
    N_2 = bin(N)[2:]

    if N % 2 == 0:
        R = '10' + N_2[2:] + '1'
    else:
        R = '11' + N_2[2:] + '01'

    if int(R, 2) > 215:
        print(N)
        break
'''

# Task 5
'''
def sum_digits(n):
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res

s = '>' + '1'*30 + '2'*20 +  '3'*10 # Нет необходимости размещать случайным образом

while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s:
        s = s.replace('>1', '111>', 1)
    elif '>2' in s:
        s = s.replace('>2', '112>', 1)
    elif '>3' in s:
        s = s.replace('>3', '123>')

print(sum_digits(int(s[:-1]))) # 230
'''

# Task 6
'''
s = 'F' * 70

while 'FFFF' in s or 'LLL' in s:
    if 'LLL' in s:
        s = s.replace('LLL', 'F', 1)
    else:
        s = s.replace('FFFF', 'L', 1)

print(s)
'''

# Task 9 # Исполнитель
'''
def F(start, stop):
    if start == stop:
        return 1 # путь найден
    elif start > stop:
        return 0 # перескочили
    return F(start+1, stop) + F(start * 2, stop) + F(start*2 + 1, stop) + F(start*10, stop)

print(F(1, 15)) # 84
'''

# Task 10
'''
def F(x, y):
    if x == y:
        return 1
    if x > y or x == 26: # исключаем число
        return 0
    return F(x+1, y) + F(2*x+1, y)

# Сколько существует таких программ, которые число 1 преобразуют в число 27,
# причём траектория вычислений обязательно содержит число 11, и не содержит число 26?

print(F(1, 11) * F(11, 27))
'''

# Task 11 # Исполнитель Калькулятор. Как с ним быть?

# x - исходное число
# c - количество команд
# TODO: не понятно...
# Тут взял аналог: https://egogo.onrender.com/task/23
'''
from functools import * # Дабы программа работа быстрее

@lru_cache(None)
def F(x, c):
    # print('progress', x, c)
    if c == 7:
        ans.add(x)
        return
    F(x+4, c+1)
    F(x-3, c+1)

ans = set() # Используем множество, т.к. речь о различных числах
F(100, 7)
print(len(ans))
'''


