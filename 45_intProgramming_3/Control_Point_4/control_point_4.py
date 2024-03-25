
# Task 2
# file 17
'''
Определите количество пар последовательности, в которых хотя бы одно число оканчивается на ту же цифру,
что и минимальный элемент последовательности кратный 25.

Гарантируется, что такой элемент в последовательности есть.

В ответе запишите количество найденных пар,
затем минимальное из произведений элементов таких пар.

В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
'''
"""
f = open('17.txt')

lines = [int(line) for line in f]

# Сначала найти минимальный эл. последовательнсти кратный 25
min_val_25 = 99999

for el in lines:
    if el > min_val_25 and el % 25 == 0:
        min_val_25 = el

# Подсчёт кол. пар в которых есть эл. оканчивающийся на ту же цифру, что и min_val_25
count = 0
min_product = 99999 # Минимальной найденное произведение

for i in range(len(lines) - 1):
    if (lines[i] % 10) == (min_val_25 % 10) or (lines[i + 1] % 10) == (min_val_25 % 10):
        count += 1
        min_product = min(min_product, lines[i]*lines[i + 1])

print(count, min_product)

f.close()
"""

# Task 3
# file 24

# Определите максимальное количество идущих подряд гласных букв, при том,
# что каждые два соседних символа должны быть различны.
'''
f = open('24.txt')
glasnie = 'AEIOUY'
# soglasnie = 'BCDFGHJKLMNPQRSTVWXYZ'
line = f.readline()

cur_len = 0
max_len = 0

for el in line:
    if el in glasnie:
        cur_len += 1
    else:
        max_len = max(cur_len, max_len)
        cur_len = 0

print(max_len)
f.close()
'''

# Task 4
# file 27A

# I have no idea how to solve this...
'''
'''






