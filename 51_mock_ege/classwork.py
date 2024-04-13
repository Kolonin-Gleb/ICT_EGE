# Task 1
# KE = 10

# Task 2
# XZYW

# Task 3
# Решение в Excel

# Task 4
# Решение на изображении

# Task 5
'''
lst = []

for N in range(4, 1000):
    bin_N = bin(N)[2:]
    if N % 4 == 0:
        bin_R = bin_N + bin_N[-3:]
    else:
        bin_R = bin_N + bin((N % 4) * 4)[2:]

    R = int(bin_R, 2)
    if R > 2024:
        lst.append(R)

print(min(lst)) # 2028
'''

# Task 6
# answer 27

# Task 7
# 43200

# Task 8

# А = 1
# Б = 2
# 3 = 3
# И = 4
# ИЗБА = 4321

# Task 9
# Решение в Excel у Миши Ответ: 607

# Task 10
# Решение в Word

# Task 11
# Решение на изображении Ответ: 32

# Task 12
'''
for n in range(4, 1000):
    s = '2' + n * '5'
    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '5', 1)
        elif '355' in s:
            s = s.replace('355', '52', 1)
        elif '555' in s:
            s = s.replace('555', '3', 1)

    if sum([int(x) for x in s]) == 17:
        print(n) # 29 # WHY not printed?
        break
'''

# Task 14
'''
x = 3*3125**8 - 4*625**6 + 3*125**5 - 2024
k = 0
while x > 0:
    if x % 24 == 6: k+=1
    x //= 24

print(k)
'''

# Task 15
'''
for A in range(1000):
    f = 1
    for x in range(300):
        for y in range(300):
            if ((x >= 12) or (3 * x < y) or (x * y < A)) == 0:
                f = 0
                break
        if f == 0:
            break
    if f == 1:
        print(A) # 364
        break
'''

# Task 16
'''
'''



# Task 17
'''
f = open('17.txt')

a = [int(i) for i in f]

m2, k, ms = 0, 0, 0
dw = [i for i in range(10, 100)]

for x in a:
    if x in dw:
        m2 = max(m2, x)

for i in range(len(a) - 1):
    x = a[i] in dw and a[i + 1] not in dw
    y = a[i + 1] in dw and a[i] not in dw
    if (x or y) and (a[i] + a[i + 1]) % m2 == 0:
        k += 1
        ms = max(ms, a[i] + a[i + 1])

print(k, ms) # 16 9702
'''

# Task 18
# Решение в Excel
# Сначала МАКС, затем МИН

# Task 19
'''
'''
# 1 Куча
# +1
# +4
# *3

# Win S >= 43
# s - тек. кол. камней
# ь - ходы
'''
def f(s, m):
    if s >= 43:
        return m%2 == 0
    if m == 0:
        return 0
    # Ещё есть ходы, что можно совершить
    h = [f(s+1, m -1), f(s+4, m -1), f(s*3, m-1)]

    return any(h) if (m-1)%2 == 0 else all(h) # Если условие победы при ошибочном ходе противника заменить all на any (только в номере 19)


# Прокрути такие s, при которых победа достигается 2ым ходом (1ый ход Вани)
print('19)', [s for s in range(1, 43) if f(s, m=2)]) # 14
# Прокрути такие s, при которых победа достигается не 1ым ходом Пети, а 3им ходом (2ый ход Пети)
print('20)', [s for s in range(1, 43) if not f(s, m=1) and f(s, m=3)]) # 10 13
# Прокрути такие s, при которых нет гарантированной победы Вани 2ым ходом
# Но он побеждает 4ым ходом
print('21)', [s for s in range(1, 43) if not f(s, m=2) and f(s, m=4)]) # 9 12
# Кол. ходов передаваемое в функ. f будет уменьшаться, чтобы найти все возможные случаи победы.
'''

# Task 22
# Параллельные процессы в Excel

# Task 23
'''
def f(x, y):
    if x > y or x == 15:
        return 0
    if x == y:
        return 1
    else:
        return f(x+1, y) + f(x+2, y) + f(x * 3, y)

print(f(1, 11) * f(11, 25)) # 22605
'''

# Task 24
'''
f = open('24.txt')     #открываем файл
a = f.readline() #считываем все символы файла, они на первой строке
E = []      #пустой массив, куда запишем индексы букв Е в исходной строке
for i in range(len(a)):    #проходим по всем индексам строки
    if a[i] == 'E': #находим буквы Е
        E.append(i) #запоминаем индекс буквы
k = 0  #переменная для определения максимальной длины подпоследовательности
for i in range(25, len(E)):  #проходим по всем возможным под-тям
    k = max(E[i] - E[i - 25] - 1, k)   #определяем максимальную длину
print(k)
f.close()
'''

# Task 25
'''
from fnmatch import *
for x in range(202400, 10**10, 2024):
    if fnmatch(str(x), "2024*4?2"):
        print(x, x// 2024)
'''

# Task 26
'''
f = open('26.txt')
n = int(f.readline())
a = []
for i in range(n):
    line = [int(x) for x in f.readline().split()]
    a.append([line[1], line[0]])
f.close()

a.sort()
k = 1
time = a[0][0] # конец 1ого мероприятия
b = []
m = 0

for i in range(1, n):
    if a[i][1] >= time:
        time = a[i][0]
        k += 1
        b.append(a[i])

for i in range(n):
    if a[i][1] >= b[-2][0]:
        m = max(m, a[i][0])
print(k, m) # 32 1299
'''

# Task 27
'''
'''

f = open(r'G:\GitHub repos\ICT_EGE\51_mock_ege\27\27B.txt') # A or B
n = int(f.readline())
k = int(f.readline())
m = 17
a = [(int(f.readline()) % m) for i in range(k)]
ostat = []

for i in range(n):
    ostat.append(a.count(i))
count = ostat[0] * (ostat[0] - 1) // 2

for i in range(1, m //2 + 1):
    k += ostat[i] * ostat[m - i]

for i in range(n - k):
    x = int(f.readline()) % m
    k += ostat[(m - x) % m]
    ostat[a.pop(0)] -= 1
    ostat[x] += 1
    a.append(x)

print(k) # 2786 # 
f.close()


