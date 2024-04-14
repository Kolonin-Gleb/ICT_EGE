# Task 1

# print(2**6)
# print(2**7)

# print(129*2)

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

print(count, min_product) # 576 -89855759

f.close()
"""

# Task 2 Mike's solution
'''
# f = open("17.txt")
# count = 0
# min_el = 10001
# min_multiply = 10**9
#
# a = [int(i) for i in f]
#
# for i in a:
#     if i % 25 == 0:
#         min_el = min(min_el, i)
# min_el = min_el % 10
#
# for i in range(len(a) - 1):
#     if a[i] % 10 == min_el or (a[i+1] % 10 == min_el):
#         count += 1
#         min_multiply = min(min_multiply, a[i] * a[i + 1] )
#
# print(count, min_multiply)
# f.close()
'''


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

# Task 3 Mike's solution
'''
f = open("24.txt")
a = f.readline()
k = 1
maxx = 1
gl = "AEIOUY"
for i in range(len(a) - 1):
    if a[i] in gl and a[i + 1] in gl and a[i] != a[i + 1]:
        k += 1
        maxx = max(maxx, k)
    else:
        k = 1

print(maxx)
f.close()
'''

# Task 4
# file 27A

# Mike's solution
'''
f = open('27A.txt')

N = int(f.readline())

arr = [int(f.readline()) for i in range(N)]

money = [0] * N

for i in range(N):
    for j in range(N):
        dist = min(abs(j - i), N - abs(j - i))
        money[i] += arr[j] * dist * 8

print(min(money))

f.close()
'''






