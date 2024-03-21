# Task 12
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ((x and not y) or (y == z) or w) == 0:
                    print(x, y, z, w)
# yxwz
'''

# Task 13
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if (z or (not x and not y) or (y == w) ) == 0:
                    print(x, y, z, w)
# zwyx
'''

# Task 1
# Для какого наименьшего целого неотрицательного числа А выражение
# (y + 7x < A) ∨ (x > 2) ∨ (y > 13)
# тождественно истинно, то есть принимает значение 1 при любых целых неотрицательных x и y?
'''
for A in range(1_000):
    flag = True
    for x in range(500):
        for y in range(500):
            if ( (y + 7*x < A) or (x > 2) or (y > 13) ) == 0:
                flag = False
                break
    if flag:
        print(A)
        break
'''

# Task 2
'''
count = 0
for A in range(1_000):
    flag = True
    for x in range(500):
        for y in range(500):
            if ( ((x < A) <= (x**2 < 81)) and ((y**2 <= 36) <= (y <= A)) ) == 0:
                flag = False
                break
    if flag:
        count += 1
        print(count)

print(count)
'''

# Task 3
'''
for A in range(1, 500): # НАТУРАЛЬНОГО А
    flag = True
    for x in range(1, 500): # НАТУРАЛЬНОГО x
        if ( (not (x % 12 == 0) or not (x % 18 == 0)) <= (not (x % A == 0)) ) == 0:
            flag = False
            break
    if flag:
        print(A)
        break
'''

# Task 4
'''
for A in range(10_000): # Неотр.
    flag = True
    for x in range(1_000):
        if ( (x&77 != 0) <= (x&12 == 0) <= (x&A != 0) ) == 0: # Проивоположное значение в пржоверке
            flag = False
            break
    if flag:
        print(A)
        break

for A in range(128):
    flag = True
    for x in range(128):
        if ((x&77==0) or (x&12!=0) or (x&A!=0))==0: # Формула упращена переходом от импликации к отрицанию
            flag=False

    if flag:
        print(A)
        break
'''

# Task 5
# x&А = 0 → ((x&23 = 0 ∨ x&18 = 0) → (x&A = 0 ∧ x&23 = 0))
'''
for A in range(1000):
    flag = True
    for x in range(500):
        if ( (x&A != 0) or ( (x&23 != 0) and (x&18 != 0) ) or ((x&A == 0) and (x&23 == 0)) ) == 0:
            flag = False
            break

    if flag:
        print(A)
        break
'''

# А  эта задача решается и без упрощения функции...
'''
for A in range(10000):
    flag = True
    for x in range(1000):
        if ((x & A == 0) <= (((x & 23 == 0) or (x & 18 == 0)) <= ((x & A == 0) and (x & 23 == 0)))) == 0: 
            flag = False
            break

    if flag == True: 
        print(A)
        break
'''

# Task 9
'''
for A in range(1, 1000): # Натуральные!
    flag = True
    for x in range(1, 500): # Натуральные!
        if ( ((x % 4 != 0) or (x % 5 != 0)) or (x + A >= 70) ) == 0:
            flag = False
            break

    if flag:
        print(A)
        break
'''

# Task 10
'''
P = list(range(8, 31))
P = [i for i in range(8, 31)] #вводим отрезок

maxx = 0 #контрзначение для максимума

for A in range(1, 10000): #цикл для перебора значений параметра А
    flag = True #флаг показывает, подходит нам параметр или нет
    for x in range(1, 1000): #цикл для перебора значений переменной х
        if ((not x + A >= 35) or (x < 15) or (not x in P)) == 0:
            flag = False #изменяем переменную-флаг, чтобы показать, что параметр не подходит
            break
    if flag == True: #проверяем, что выражение всегда было =1
        maxx = max(maxx, A) #поиск наибольшего подходящего A

print(maxx) #выводим наибольшее подходящее значение
'''

# Task 11
'''
'''
