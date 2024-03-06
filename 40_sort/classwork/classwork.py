# Сортировка в Python

# Задание 26 на 2 балла

# Task 1
'''
f = open("1.txt") # 
a = f.readline().split() # считывание 1ой строки
n = int(a[0]) # кол. участников
k = int(a[1]) # кол. победителей
m = int(a[2]) # кол. призёров
# Кол. участников не вводится!!!

a = [int(i) for i in f] # Записываем все числа в массив
a.sort(reverse=True)    # счёт по убыванию

# print("min score winner", "max score participant")
print(a[k + m - 1], a[k + m]) # 825 821
f.close()
'''

# Task 2
'''
# В ответе:
# 1 - стоимость покупки с учётом скидки
# 2 - стоимость самого дорогого товара

# Будем делать скидку на самые дешёвые товары
# чтобы итоговый чек получился максимальным
'''
# import math
# math.round(summa) -- doesn't exist
"""
f = open('2.txt')
n = int(f.readline()) # кол. всего товаров
S = 0 # Сумма товаров без скидки
disount = [] # стоимости товаров на которые нужно дать скидку

for i in range(n):
    x = int(f.readline())
    if x > 120:
        disount.append(x) # все товары, на которые возможна скидка (> 120)
    else:
        S += x

disount.sort()
half = len(disount) // 2 # число товаров на которые будем давать скидку
skidka = disount[:half] # на эти товары будет применена скидка
not_skidka = disount[half:]

summa = 0 
summa = S + sum(skidka) * 0.75 + sum(not_skidka)
print(summa, skidka[-1])
"""

# Task 3
'''
f = open('3.txt')
n = int(f.readline())
elements = [int(i) for i in f]
K_skidka  = n // 4

elements.sort(reverse=True)
summ_Pete = sum(elements[:K_skidka]) * 0.5 + sum(elements[K_skidka:])

elements.sort()
sum_shop = sum(elements[:K_skidka]) * 0.5 + sum(elements[K_skidka:])

print(summ_Pete, sum_shop)
f.close()
'''

# Task 4 
# Задача на матрёшку
'''
f = open('4.txt')
n = int(f.readline())
a = [int(i) for i in f]
a.sort(reverse=True)

k = 1
last = a[0]
for i in range(len(a)):
    if last - a[i] >= 2: # условие
        k += 1
        last = a[i] # Обновляем длину последней коробки

print(k, last) # 3872 79
f.close()
'''

# Двумерные массивы
'''
# Initialization
a = [[1014, 1200],
[40, 1000],
[61, 1000],
[30, 60],
[59, 70]]

# Getting elements
print(a[0])    # [1014, 1200]
print(a[0][0]) # 1014
print(a[0][1]) # 1200
print(a[0][1]) # 1200
print(a[3][1]) # 60

# Len
print(len(a))    # 5
print(len(a[0])) # 2

num =  ["1", "2", "3"]
int_num = list(map(lambda x: int(x), num))
print(int_num)

sum = lambda x, y: x + y
result = sum(5, 3)
print(result)
'''

# Task 5*
# TODO: не работает!
'''
with open('5.txt', 'r') as f:
    k = int(f.readline().strip())
    n = int(f.readline().strip())
    baggage = []
    for line in f:
        x = list(map(int, line.split()))
        baggage.append(x)

    baggage.sort(key= lambda x: x[0])
    cell = [0] * k

    count = 0
    number = 0

    for time in baggage:
        for i in range(k):
            if time[0] > cell[i]:
                cell[i] = time[i]
                count += 1
                number = i + 1
                break

print(number, count) # 53 340
'''
