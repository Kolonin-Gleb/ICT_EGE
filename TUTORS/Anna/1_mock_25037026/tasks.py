# Task 2
'''
print("x, y, z, w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if (y and (x or z) or not(y or z) or w) == 0:
                    print(x, y, z, w)
# Answer: xywz
'''

# Task 5
'''
a = []
for n in range(1, 100):
    s = bin(n)[2:] # перевод в двоичную систему
    s = str(s)

    if n % 2 == 0:
        s = s + s[-2:]
    else:
        s = "1" + s + "0"
    r = int(s, 2) # перевод в десятичную систему

    if r < 100:
        a.append(n)
print(max(a))
'''

# Task 6
'''
def build_R(N):
    binary_N = bin(N)[2:]  # Получаем двоичное представление числа N, убирая префикс '0b'
    
    if N % 2 == 0:  # Если число N чётное
        R_binary = binary_N + binary_N[-2:]  # Дописываем две последние цифры
    else:           # Если число N нечётное
        R_binary = '1' + binary_N + '0'  # Добавляем '1' в начало и '0' в конец
    
    R_decimal = int(R_binary, 2)  # Переводим двоичное представление в десятичное
    return R_decimal

for N in range(1_000_000):
    R = build_R(N)
    if R < 100:
        print("Число R:", R)
    else:
        print(N - 1)
        break
'''

# Task 12
# Непридумал
"""
n = 10_000 # [3; 10_000] # Сразу беру максимум, раз нужна наибольшая сумма.
s = '3' + '5' * n

max_sum = 0

for i in range(n):
    while '333' in s or '555' in s:
        if '555' in s:
            s = s.replace('555', '3', 1)
        else:
            s = s.replace('333', '5', 1)


    print(s)
"""

# Task 9

# ОБА УСЛОВИЯ!!!
# — в строке есть ровно три числа, каждое из которых повторяется дважды, и одно число без повторений;
# — среднее арифметическое минимального и максимального СРЕДИ повторяющихся чисел строки < неповторяющегося числа val(k1).
# Только число (строк)
# узнаём сколько строк в файле # 12_000
f = open('9_12241.csv')
k = 0
for i in range(12000):
    lst = list(map(int, f.readline().split(',')))
    k1 = 0 # значение уникального числа
    k2 = 0 # кол. элементов входящих 2 раза
    for i in set(lst): # i - элемент множнество. Уникальные
        if lst.count(i) == 2: # повторяется дважды в числе!
            k2 += 1
        elif lst.count(i) == 1: # число без повторений
            k1 = i
    if k2 == 3: # Первое условие пройдено!
        #  and k1 > 0
        lst.remove(k1) # Убираем известное значение k1
        if (min(lst) + max(lst)) / 2 < k1: # Второе условие
            k += 1
print(k) # 3382

# Task 13
'''
'''

# Task 14
'''
'''

# Task 16
'''
def F(n):
    if n <= 3:
        return 1
    else:
        return (n + 3) * F(n - 2)

print(F(2028) / F(2024))
'''



# Task 8
'''
from itertools import *
# Найти количество

# 5 - once!!
# doesn't start with 0
k = 0
for i in product('012345678', repeat=5):
    flag = 1
    s = ''.join(i)
    if s[0] != '0' and s.count('5') == 1:
        for j in range(len(s) - 1):
            if s[j] == s[j + 1]:
                flag = 0
                break
        if flag:
            k += 1

print(k) # 13377
'''

# Task 8 another solution
"""
from itertools import *
# Найти количество

# 5 - once!!
# doesn't start with 0
k = 0
for i in product('012345678', repeat=5):
    flag = 1
    s = ''.join(i)
    if s[0] != '0' and s.count('5') == 1:
        if s[0] != s[1] and s[1] != s[2] and s[2] != s[3] and s[3] != s[4]:
            k +=1 

print(k) # 13377
"""

