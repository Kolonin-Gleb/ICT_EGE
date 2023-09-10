# Task 4
'''
n = 3 # количество чисел
mina = 999999

for i in range(n):
    num = int(input())
    if num < mina:
        mina = num

print(mina)
'''

# Task 5
'''
lst = int(input()), int(input()), int(input())
num_lst = list(map(int, lst))
print(max(num_lst) - min(num_lst))
'''

# Task 6
'''
n = int(input()) # Количество чисел
mina = 999999

for i in range(n):
    num = int(input())
    if num < mina:
        mina = num

print(mina)
'''

# Task 7
'''
n = int(input()) # Количество чисел
maxa = -1

for _ in range(n):
    num = int(input())
    if num % 3 == 0:
        if maxa < num:
            maxa = num

print(maxa)
'''

# Task 8
'''
n = int(input()) # Количество чисел
maxa = -1

for _ in range(n):
    num = int(input())
    if num % 5 == 0 and not num % 10 == 0:
        if maxa < num:
            maxa = num

print(maxa)
'''

# Task 9 
'''
n = int(input()) # Количество чисел

summa = 0
max_even = -99999999
min_odd = 99999998

for _ in range(n):
    num = int(input())
    summa += num

    if num % 2 == 0:
        if max_even < num:
            max_even = num
    else:
        if min_odd > num:
            min_odd = num

if max_even * min_odd == summa:
    print("Повезло")
else:
    print("В следующий раз")
'''

# 
'''
'''
