# 25037844 Вариант
# Task 1 = 17 # Граф +

# Task 2 = 
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ((x or (not y)) and (not (x == z)) and w) == 1: # значение F из таблицы!
                    print(x, y, z, w)
'''
# Ответ: WZYX
'''
x y z w
0 0 1 1
1 0 0 1
1 1 0 1
'''

# Task 5
'''
lst = []
for N in range(1, 1000):
    bin_N = bin(N)[2:]
    
    bin_R = bin_N + str(bin_N.count('1') % 2)
    bin_R = bin_R + str(bin_R.count('1') % 2)

    R = int(bin_R, 2)

    if R > 60:
        lst.append(R)

print(min(lst)) # 66
'''

# Task 6 # Turtle
'''
from turtle import *
# settings
k = 40
screensize(1000, 1000)
tracer(0)
left(90)

# move
right(90)
for i in range(9):
    forward(5*k)
    right(120)
penup()

# grid
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x*k, y*k)
        dot(5, 'blue')

done() # 8
'''

# Task 8
'''
count = 0
for b1 in sorted("ВЗГЛЯД"):
    for b2 in sorted("ВЗГЛЯД"):
        for b3 in sorted("ВЗГЛЯД"):
            for b4 in sorted("ВЗГЛЯД"):
                s = b1+b2+b3+b4
                if s.count('З') in [1, 2]:
                    # print(s)
                    count += 1
                # if count  == 10:
                    # break

print(count) # 650
'''

# Task 11
# print(2**4)
# print(2**5)

# Task 12
'''
# s = '>' + '4' * 50 # TODO: Дан пример, который нельзя прогнать!!!

s = '>' + '1' * 11 + '2' * 12 + '3' * 30
# Определить сумму после обработки
while '>1' in s or '>2' in s or '>3' in s:
    if ">1" in s:
        s = s.replace('>1', '22>', 1)
    elif ">2" in s:
        s = s.replace('>2', '222>', 1)
    elif '>3' in s:
        s = s.replace('>3', '1>', 1)

summa = 0
for el in list(s[:-1]):
    summa += int(el)

print(summa) # 146
'''

# Task 13
'''
net   = '192.168.64.176'
mask  = '255.255.255.240'
print(bin(176)[2:].zfill(8))
print(bin(240)[2:].zfill(8))
# 4 нуля
print(2**4//2) # Ответ: 8
'''

# TODO: Task 14
'''
def dec_to_4(n):
    res = ''
    while n > 0:
        res = str(n % 4) + res
        n //= 4
    return res

number = 16**820 - 2**761 + 14

print(dec_to_4(10)) # 22 test passed
print(dec_to_4(number)) #3784
print(dec_to_4(number).count("0")) # т.к. все нули значащие = 378
'''

# Task 15
# Данный можно решить кодом
'''
for A in range(10_000):
    flag = 0
    for x in range(10_000):
        # if ( (x&A != 0 ) <= (((x&17 == 0) and (x&5 == 0)) <= (x&3 != 0))) ==0:
        if ( (x&A != 0 ) <= (((x&17 == 0) and (x&5 == 0)) <= (x&3 != 0))) == 0: # прот. знач.
            flag = 1
            break
    if flag == 0:
        print(A)
'''

# Task 16
'''
def F(n):
    if n <= 2:
        return 1
    return F(n - 1) + 2 * F(n - 2)

print(F(17)) # 43691
'''

# Task 17
'''
f = open('17_2388.txt')
# f = open('test.txt')

data = [int(x) for x in f]

min_positive_summa = 999999999
pair_counter = 0

# Рассмотрение пар
for i in range(len(data) - 1):
    if (data[i] % 5 == 0 and data[i + 1] % 5 == 0) and (data[i] % 3 != 0 and data[i + 1] % 3 != 0):
        pair_counter += 1
        cur_pair_sum = data[i] + data[i+1]
        if cur_pair_sum > 0:
            min_positive_summa = min(min_positive_summa, cur_pair_sum)

print(pair_counter, min_positive_summa) # 93, 15

f.close()
'''

# Task 18 Робот сборщик монет
'''
Команды:
- Вправо
- Вверх

МИН затем МАКС
'''

# Task 19 ТЕОРИЯ ИГР!!
'''
1 Куча
Ходы:
+2
*3
Win S >= 50 and S <= 119 - Победил последний сделавший ход
Иначе побеждает проитивник!!!
'''

# s - тек. кол. камней
# m - ход
"""
def f(s, m):
    if s >= 50 and s <= 119: # молодец!
        return m % 2 == 0
    if s > 119:
        return m % 2 != 0 # побеждает соперник при сильном превышении
    elif m == 0:
        return 0
    # Перебираем все ходы
    h = [f(s+2, m-1), f(s*3, m-1)]

    return any(h) if (m-1)%2 == 0 else all(h)

# Найти кол. S, при которых Ваня выигрывате 1ым ходом
# В () range указывать диапазон возможных стартовых размеров куч!
print("19)", [s for s in range(1, 50) if f(s, 2)]) # 3
print("20)", [s for s in range(1, 50) if not f(s,1) and f(s, 3)]) # 14
print("21)", [s for s in range(1, 50) if not f(s,2) and f(s, 4)]) # 12 / 43
"""

# Task 22 Параллельные процессы

# Task 23
'''
def f(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1

    return f(x+1, y) + f(x+2, y) + f(x*2, y)


print(f(4, 9) * f(9, 12) * f(12, 15)) # 81
'''

# Task 24
'''
f = open('24_2393.txt')
data = f.readline()
f.close()

max_len_rising = 1
cur_len_rising = 1

for i in range(len(data) - 1):
    if int(data[i]) <= int(data[i+1]):
        cur_len_rising += 1
    else:
        max_len_rising = max(max_len_rising, cur_len_rising)
        cur_len_rising = 1

print(max_len_rising) # 49
'''

# Task 25
# Функция для получения делителей числа
'''
Назовём маской числа последовательность цифр,
в которой также могут встречаться следующие символы:
— символ «?» означает ровно одну произвольную цифру;
— символ «*» означает любую последовательность цифр произвольной длины;
в том числе «*» может задавать и пустую последовательность.

Например, маске 123*4?5 соответствуют числа 123405 и 12300405.

Среди натуральных чисел, не превышающих 10^8,
найдите все числа, соответствующие маске 12*34?5, делящиеся на 2025 без остатка.
В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания,
а во втором столбце — соответствующие им результаты деления этих чисел на 2025.
'''

# from fnmatch import *
# for x in range(0, 10**8, 2025):
#     if fnmatch(str(x), '12*34?5'):
#         print(x, x//2025)
