# var 7 type 15
'''
def is_triangle(n, m, k):
    return n + m > k and n + k > m and m + k > n

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if (not(is_triangle(x, 11, 18) == ((not(max(x, 5) > 15)))) and is_triangle(x, A, 5)) == False:
            flag = False
    if flag:
        print(A) # Должен быть вывод 25, но у меня его нет (-_-)
        break
'''

# var 7 type 16
# ChatGPT helped
'''
from sys import setrecursionlimit
setrecursionlimit(9999)

def F(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 != 0:
        return F(n-1) + F(n-2)
    if n > 2 and n % 2 == 0:
        return sum(F(i) for i in range(1, n)) # 887040
        # for i in range(n):
        #     return F(i)
print(F(24)) # 887040
'''

# 19-21 Game theory
'''
2 Кучи:
+2
*3

Победа при (a + b) >= 52

Размеры куч:
a = 5
1 <= b <= 46
'''
"""
def F(a, b, m):
    if (a + b) >= 52:
        return m % 2 == 0
    if m == 0:
        return 0
    h = [F(a+2, b, m-1), F(a*3, b, m-1), F(a, b+2, m-1), F(a, b*3, m-1)]

    return any(h) if (m-1)%2 == 0 else all(h) #  2th all to any (for unlucky moves)

# print("19)", [b for b in range(1, 47) if not F(5, b, 1) and F(5, b, 2)]) # minS = 6
print("20)", [b for b in range(1, 47) if not F(5, b, 1) and F(5, b, 3)]) # 2 minS = 5 6
print("21)", [b for b in range(1, 47) if not F(5, b, 2) and F(5, b, 4)]) # 14 
"""

# Task 24
'''
f = open('24_6054.txt')
line = f.readline()
f.close()
line = line.replace('A', '0').replace('B', '1').replace('C', '1')
line = line.replace('110', '*')

max_seq = 0
seq = 0

for el in line:
    if el == '*':
        seq += 3
    else:
        max_seq = max(max_seq, seq)
        seq = 0

# Для подстраховки, если макс. последовательность будет последней
max_seq = max(max_seq, seq)
print(max_seq) # 6
'''

# Task 25
'''
from fnmatch import fnmatch

for x in range(0, 10**7, 159):
    if fnmatch(str(x), '2?1*67'):
        print(x, x//159)
'''

# Task 26 - этот можно в Excel

# Task 27
'''
f = open('27_A_6057.txt')
N = f.readline()
f.close()
'''
