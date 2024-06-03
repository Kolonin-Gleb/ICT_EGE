# Task 1 - board.png

# Task 2
'''
print("x y z w")

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ( ((x <= y) == (z <= w)) or (x and w) ) == 0:
                    print(x, y, z, w)
'''
# zyxw
"""
x y z w
0 0 1 0
0 1 1 0
1 1 1 0
1 0 0 0 - extra
"""

# Task 3 - Excel

# Task 4 - Excel (draw + table)

# Task 5
'''
result_set = set()
for N in range(10, 1001):
    N_2 = bin(N)[2:]

    if '1' in N_2:
        N_2 = N_2.replace('1', '*', 1) # 
        to_be_replaced = '*'
        while (to_be_replaced+'0') in N_2:
            to_be_replaced += '0'
        N_2 = N_2.replace(to_be_replaced, '', 1)
        if len(N_2) == 0:
            N_2 = "0" # верно?
    result_set.add(N - int(N_2, 2))

print(len(result_set)) # Кол. различных значений = 7
'''

# Task 6
'''
from turtle import *
screensize(500, 500)
tracer(0)
left(90)
k = 30

for x in range(4):
    forward(8*k)
    right(90)

setpos(0, 0) # Наверное нужно вернуться в исходную точку

color('red') # Буду считать точки вне красной зоны
for x in range(3):
    forward(12*k)
    right(120)

penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x*k, y*k)
        dot(4, 'blue')
# Помни: Точки на линии тоже не учитывать
done() # Итого точек = 12 (ВЕРНЫЙ 13)
'''

# Task 7 - board/paper

# Task 8
'''
counter = 0
for b1 in "МАТВЕ":
    for b2 in "МАТВЕЙ":
        for b3 in "МАТВЕЙ":
            for b4 in "МАТВЕЙ":
                for b5 in "МАТВЕЙ":
                    for b6 in "МАТВЕЙ":
                        word = b1+b2+b3+b4+b5+b6
                        if 'АЕ' in word or len(set(word)) != 6:
                            continue
                        counter += 1
print(counter) #504
'''

# Task 9 - Excel

# Task 10 - Word

# Task 11 - board/paper

# Task 12
'''
s = '9'*1000

while '999' in s or '888' in s:
    if '888' in s:
        s = s.replace('888', '9', 1)
    else:
        s = s.replace('999', '8', 1)

print(s) #8899
'''

# Task 13 IP
# from ipaddress import ip_network
# New condition type 
# Лучше решу из книги Крылова аналогичный номер


# Task 14
'''
num = 4**2020 + 2**2017 - 15
num_2 = bin(num)[2:]
print(num_2.count('1')) #2015
'''

# Task 15
# Подсмотрел шаблон и Решени
'''
def f(x,a): 
    return ((x in a) <= (x**2 <= 100)) and ((x**2 <= 64) <= (x in a))
 
a = set([i for i in range(-1000,1000)])

for x in range(-1000, 1000):
    if not f(x,a):
        a.remove(x)
print(len(a) - 1)
'''

# Task 16
'''
def F(n):
    if n == 1:
        return 1
    return F(n-1)+n

print(F(40)) #820
'''

# Task 17
'''
f = open('17.txt')
data = [int(el) for el in f]
f.close()

avg_of_even = []
for el in data:
    if el % 2 == 0:
        avg_of_even.append(el)

avg_of_even = sum(avg_of_even) // len(avg_of_even)
pair_counter = 0
max_pair_sum = 0

for i in range(len(data) - 1):
    if ((data[i] % 3 == 0) or (data[i + 1] % 3 == 0)) and \
        (data[i] < avg_of_even or data[i + 1] < avg_of_even):
        pair_counter += 1
        max_pair_sum = max(max_pair_sum, (data[i] + data[i + 1]))

print(pair_counter, max_pair_sum) #2288 14875
'''

# Task 18 - Excel labirint

# Task 19-21 Game Theory
"""
1 Куча
Ходы:
+1
+4
*5

Победа S >= 68
Изначально 1 ≤ S ≤ 67
"""
'''
'''

def F(s, m):
    # усл. победы
    if s >= 68:
        return m % 2 == 0
    # усл. выхода
    if m == 0:
        return 0
    # Рассчитать все варианты ходов
    h = [F(s+1, m-1), F(s+4, m-1), F(s*5, m-1)]
    return any(h) if (m-1) %2 == 0 else all(h)


print("19)", [s for s in range(1, 68) if F(s, )]) # Победа Вани после неудачного хода Пети
print("20)", "") # 
print("21)", "") # 



# Task 22 - Excel

# Task 23
'''
def F(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return F(x+1, y) + F(x+2, y) + F(x*2, y)


print(F(3, 10) * F(10, 12)) #60
'''


# Task 24
# Подсмотрел решение
'''
f=open('24.txt').readline().split('XZZY')
maxi=0
for i in range (0,len(f)):
    maxi=max(len(f[i])+6,maxi) # +6, т.к. слева и справа можжет быть не полная последовательность по которой делили
print(maxi) # Вообще с маленькой вероятностью это ни так, но можем пренебречь этим???
# Ответ 1713
'''

# Task 25
# Новое условие.
# Лучше решу из книги Крылова аналогичный номер


# Task 26 - ??
'''
'''
