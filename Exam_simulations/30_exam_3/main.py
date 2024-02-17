# Task 2
'''
print("x, y, z, w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ((x and not(y)) or (y == z) or not(w)) == 0:
                    print(x, y, z, w)
# xwzy
'''

# Task 3
'''
'''

# Task 5
'''
for N in range(1, 1000):
    bin_N = bin(N)[2:]
    bin_R = 0

    if N % 2 == 0:
        bin_R = '1' + bin_N + '0'
    else:
        bin_R = '11' + bin_N + '10'

    R = int(bin_R,2)
    if R < 264:
        print(R)
# R = 252
'''

# Task 12
'''
На вход этой программе подается строка, состоящая из 101 цифры;
последняя цифра в строке — цифра 1, а остальные цифры — восьмёрки.
Какая строка получится в результате применения программы к этой строке? В ответе запишите полученную строку.
'''

"""
s = '8' * 100 + '1'

while '133' in s or '881' in s:
    if '133' in s:
        s = s.replace('133', '81', 1)
    else:
        s = s.replace('881', '13', 1)
        print(s)

print("=============")
print(s)
"""

# Task 14
'''
for x in '0123456789ABCD':
    if ( int(f"2023{x}", 14) - int(2*f"{x}{x}", 14) ) % 5 == 0:
        print(x)
        print(int(f"2023{x}", 14) - int(2*f"{x}{x}", 14) / 5)
        break
'''

# Task 15
'''
A = 1
for A in range(10_000, 0, -1):
    flag = 1
    for x in 1, 1000:
        for y in 1, 1000:
            if ((x*y > A) or (x > y) or (8 > x)) == 1:
                print(A)
                exit()
'''

# Task 16
'''
def F(n):
    if n < 3:
        return n
    elif n >= 3 and n % 5 == 0:
        return F(n - 3) + 3*F(n - 4) + F(n - 2)
    elif n >= 3 and n % 10 == 3:
        return 10 + F(n - 1)
    else:
        return 2*F(n - 2) + F(n - 1)

print(F(17)) # 33119
'''

# Task 17
'''
with open('17.txt') as file:
    min_ends_3 = 99999999999993
    pair_sums = []

    vals = file.readlines()
    vals = [int(val[:-1]) for val in vals]

    for val in vals:
        if val % 10 == 3:
            min_ends_3 = min(val, min_ends_3)

    # Проход по парам
    count = 0
    for i in range(len(vals) - 1):
        if (vals[i] % min_ends_3 == 0 and vals[i + 1] % min_ends_3 != 0) or (vals[i] % min_ends_3 != 0 and vals[i + 1] % min_ends_3 == 0):
            count += 1
            pair_sums.append(vals[i] + vals[i + 1])

    print(count)
    print(max(pair_sums))
'''

# Task 23 # Вычислитель
'''
source = 1
res = 24
inc = 12
notinc = 18

print()
'''


# Task 24
'''
'''


