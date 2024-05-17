# ==================== TYPE 12

# 4617
'''
s = '9'*84

while '33333' in s or '999' in s:
    if '33333' in s:
        s = s.replace('33333', '99', 1)
    else:
        s = s.replace('999', '3', 1)

print(s) # 33
'''

# 9743
'''
for n in range(3, 10_001):
    s = '5' + '2'*n
    while '72' in s  or '522' in s or '2222' in s:
        if '72' in s:
            s = s.replace('72', '2', 1)
        if '522' in s:
            s = s.replace('522', '27', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
    summa = 0
    for el in s:
        summa += int(el)
    if summa == 63:
        print(n) #186
        break
'''

# 9781
'''
sums_lst = []
for n in range(3, 10_001):
    s = '1' + '2'*n
    while '12' in s  or '322' in s or '222' in s:
        if '12' in s:
            s = s.replace('12', '2', 1)
        if '322' in s:
            s = s.replace('322', '21', 1)
        if '222' in s:
            s = s.replace('222', '3', 1)
    summa = 0
    for el in s:
        summa += int(el)
    sums_lst.append(summa)

print(max(sums_lst)) # 17
'''

# 14947
'''
sums_lst = []
for n in range(3, 10_001):
    s = '1' + '9'*n
    while '19' in s  or '49' in s or '999' in s:
        if '19' in s:
            s = s.replace('19', '9', 1)
        if '49' in s:
            s = s.replace('49', '91', 1)
        if '999' in s:
            s = s.replace('999', '4', 1)
    summa = 0
    for el in s:
        summa += int(el)
    sums_lst.append(summa)

print(max(sums_lst)) # 23
'''

# ==================== TYPE 14

# 230
'''
num = 8**740 - 2**900 + 7

num = bin(num)[2:]
print(num)
# 897
'''


# 9745
'''
for x in '0123456789ABCDEFGHI'[::-1]:
    num = int(f"98{x}79641", 19) + int(f"36{x}14", 19) + int(f"73{x}4", 19)
    if num % 18 == 0:
        print(num // 18) # 470402599
        break
'''

# 15328
'''
for x in "0123456789ABCDEFGHIJKLMNOPQ"[::-1]:
    num = int(f'123{x}24', 27) + int(f'135{x}78', 27)
    if num % 26 == 0:
        print(num // 26) # 1213206
        break
'''
# import string
# print(string.ascii_letters)

# 6846
# Особая задача. Имеем дело с чрезвычайно большими С.С.
'''
for x in range(98):
    num1 = 5*98**0 + 4*98**1 + x*98**2 + 2*98**3 + 1*98**4
    num2 = 8*123**0 + 9*123**1 + x*123**2 + 1*123**3
    result = num1 + num2
    if result%123 == 0:
        print(result//123) # 792604
'''

# ==================== TYPE 15

# 760
'''
for A in range(1, 10_001):
    flag = True
    for x in range(1, 10_001):
        if ( ((x % A == 0) and (x % 16 == 0)) <= ((x % 16 != 0) or (x % 24 == 0)) ) == 0:
            flag = False
    if flag:
        print(A) # 3
'''

# 9838
'''
for A in range(10_001):
    flag = True
    for x in range(101):
        for y in range(101):
            if ( (x + 2*y > A) or (y < x) or (x < 30) ) == 0:
                flag = False
    if flag:
        print(A) # max - last
        # 89
'''

# 1223
# Особый случай ТИПа 15.
# Работа с отрезками
'''
# Цель: Найти наименьшую длину А
A = []
B = list(range(25, 40+1))
C = list(range(12, 33+1))

for x in range(1, 100): # Перебираю x в диапозоне выходящем за мин и макс эл из A, B списков
    if ( ((x in B) <= (x in A)) and ((not (x in C)) or (x in A)) ) == 0: # Противоположное значение
        A.append(x)

print(max(A) - min(A)) # 28
'''

# 15330
# Цель: Найти наименьшую длину А
'''
A = []
B = list(range(24, 90+1))
C = list(range(47, 115+1))

for x in range(1, 150):
    if ( (x in C) <= (((not(x in A)) and (x in B)) <= (not (x in C))) ) == 0:
        A.append(x)

print(max(A) - min(A)) #43
'''

# TODO: 1072 НАУЧИТЬСЯ РЕШАТЬ КОДОМ!
# Особый случай ТИПа 15.
# Работа с множествами
'''
P = set([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
Q = set([1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31])
A = set()

for x in range(-100, 100):
    if ( ((x in A) <= (x in P)) and ((x in Q) <= (not (x in A))) ) == 0:
        A.add(x)

print(A) # 10
'''

# ==================== TYPE 16

# 4621
'''
def F(n):
    if n < 3:
        return 2
    if n > 2 and n % 2 == 0:
        return 2 * F(n-2) - F(n-1) + 2
    if n > 2 and n % 2 != 0:
        return 2 * F(n-1) - F(n-2) - 2
    
print(F(17)) #358
'''

# 9839
'''
import sys
sys.setrecursionlimit(9999)

def F(n):
    if n < 3:
        return 3
    return 2 * n + 5 + F(n-2)

print(F(3027) - F(3023)) #12114
'''

# 8561
'''
def G(n):
    if n > 100:
        return n
    return G(n + 2) + 1

def F(n):
    if n <= 1:
        return n
    if n > 1 and (n % 3 == 0):
        return F(n-1) + F(n-2) + 1
    return G(n-3)

print(F(15) + F(12)) #593
'''

# ==================== TYPE 23

# 4626
'''
def F(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    return F(x-2, y) + F((x//2), y)

print(F(28, 10) * F(10, 1)) # 36
'''

# 9752
'''
def F(x, y):
    if x > y or x == 17:
        return 0
    if x == y:
        return 1
    return F(x+2, y) + F(x+3, y) + F(x*2, y)

print(F(3, 10) * F(10, 25)) #90
'''

# 9844
'''
def F(x, y):
    if x < y or x == 7:
        return 0
    if x == y:
        return  1
    return F(x-1,y) + F(x-3, y) + F(x//2, y)

print(F(19, 10) * F(10, 3)) #133
'''
