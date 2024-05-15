# Task 2
'''
print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ( (x <= y) or (not(w <= z)) ) == 0:
                    print(x, y, z, w)
'''
"""
x y z w
1 0 0 0
1 0 1 0
1 0 1 1
"""
# XZWY

# Task 5
'''
answer_lst = []

for N in range(1, 1_001):
    N_2 = bin(N)[2:]
    R_2 = ''
    if N_2.count('1') % 2 == 0:
        R_2 = N_2 + '0'
        R_2 = '100' + R_2[3:]
    else:
        R_2 = N_2 + '1'
        R_2 = '111' + R_2[3:]
    
    R = int(R_2, 2)
    # print(R) #for check
    if R >= 63:
        answer_lst.append(N)

print(min(answer_lst)) # 19
'''

# Task 6
'''
from turtle import *
screensize(4000, 4000)
tracer(0)
left(90)
k = 20


for i in range(4):
    forward(13*k)
    right(270)
penup()

backward(-4*k) # - включать?
left(90)
forward(4*k)
left(90)
pendown()

for i in range(2):
    forward(7*k)
    right(90)
    forward(17*k)
    right(90)

penup()
for x in range(-25, 25):
    for y in range(-25, 25):
        setpos(x*k, y*k)
        dot(5, 'blue')

done() # 50
'''

# Task 8
'''
counter = 0
for b1 in "012345678":
    for b2 in "012345678":
        for b3 in "012345678":
            for b4 in "012345678":
                for b5 in "012345678":
                    word = b1+b2+b3+b4+b5
                    if len(set(word)) == 5:
                        odd_counter = 0
                        for el in word:
                            if int(el) % 2 != 0:
                                odd_counter += 1
                        if odd_counter == 1:
                            counter += 1

print(counter) #2400
'''

# Task 9 (excel)
# Answer = 621

# Task 10 (word)
'''
всего без учёта регистра
что = 468

как отдел слово 
что = 431

Разность = 37
'''
# Answer = 37

# Task 12
'''
for n in range(5, 10_001):
    s = '2' + '3'*n

    while '13' in s or '233' in s or '3333' in s:
        if '13' in s:
            s = s.replace('13', '3', 1)
        if '233' in s:
            s = s.replace('233', '32', 1)
        if '3333' in s:
            s = s.replace('3333', '2', 1)
    if s.count('3') == 4:
        print(n) # 15
        break
'''

# Task 13
'''
from ipaddress import ip_network

counter = 0
for ip in ip_network('190.231.153.224/255.255.255.240', strict=False):
    adr = bin(int(ip))[2:]
    if adr.count('0') % 2 == 0:
        counter += 1

print(counter) # 8
'''

# Task 14
'''
for x in "0123456789ABCDE"[::-1]:
    num = int(f"AA{x}", 15) + int(f"BB{x}", 15) + int(f"2023", 15)
    if num % 3 == 0:
        print(num // 3) # 3949
        break
'''

# Task 15
'''
for A in range(1, 10_001):
    flag = True
    for x in range(1, 10_001):
        if ( (x % 7 == 0) <= ((x % 4 == 0) <= (not(A + x < 173))) ) == 0:
            flag = False
    if flag:
        print(A) # 145
        break
'''

# Task 16
'''
def F(n):
    if n < 1000:
        return 1
    return n**2 + F(n-1)

print(F(1775) - F(1770)) # 15717655
'''

# Task 17
'''
f = open('17.txt')
data = [int(el) for el in f]
f.close()

pair_counter = 0
max_pair_sum   = -99999999999999
max_aliquot_13 = -99999999999999

for el in data:
    if el % 13 == 0:
        max_aliquot_13 = max(max_aliquot_13, el)

last_symbol = max_aliquot_13 % 10

for i in range(len(data) - 1):
    if (data[i] % 10 == last_symbol and data[i + 1] % 10 != last_symbol) or (data[i + 1] % 10 == last_symbol and data[i] % 10 != last_symbol):
        pair_counter += 1
        max_pair_sum = max(max_pair_sum, (data[i] + data[i + 1]))

print(pair_counter, max_pair_sum) # 856 1890
'''

# Task 18 (excel)
# 607 | 1413

# Task 19 - 21 Game Theory
'''
1 куча

Ходы:
+5
*3

Win S >= 75

s = range(1, 71)
'''
# s - тек. куча
# m - ходы
"""
def F(s, m):
    if s >= 75:
        return (m % 2) == 0
    elif m == 0:
        return 0
    # все возможные ходы
    h = [F(s+5, m-1), F(s*3, m-1)]

    return any(h) if (m-1)%2 == 0 else all(h) # second all <-> any when unlucky move

# print("19)", [s for s in range(1, 71) if F(s, 2)]) # min S = 9
print("20)", [s for s in range(1, 71) if not F(s, 1) and F(s, 3)]) # 7 8 ...
print("21)", [s for s in range(1, 71) if not F(s, 2) and F(s, 4)]) # 10
"""

# Task 23
'''
def F(x, y):
    if x < y or x == 12:
        return 0
    if x == y:
        return 1
    return F(x-1, y) + F(x-3, y) + F(x%3, y)


print(F(33, 25) * F(25, 3)) # 13949
'''

# Task 24
# TODO: Почему принт не работает?
'''
'''

f = open('24.txt')
line = f.readline()
line = line.replace('23', 'X')
line = line.replace('32', 'X')
line = line.replace('0', '1').replace('2', '1').replace('3', '1').replace('4', '1').replace('5', '1').replace('6', '1').replace('7', '1').replace('8', '1').replace('9', '1')
f.close()


max_seq_found = '111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'

print(line[line.find(max_seq_found)-1:line.find(max_seq_found)+len(max_seq_found)+1])
# Определите максимальное количество идущих подряд символов, среди которых нет цифр 2 и 3, стоящих рядом.
# *Если по краям Х, то можно их убрать и прибавить 2 к общей сумме цифр


# Task 25
'''
from fnmatch import fnmatch

for x in range(0, 10**9, 44):
    if fnmatch(str(x), '2023?00*8'):
        print(x, x//44)
'''
"""
20237008 459932
202320008 4598182
202340028 4598637
202360048 4599092
202380068 4599547
"""
