# Course Book page 92
# Task 1
'''
# a)
with open("1.txt") as file:
    a = file.readline()
    k1 = 0
    for i in range(len(a)-1):
        if a[i]+a[i+1] == '31':
            k1 += 1
    print(k1)
    # b)
    k2 = a.count('31')
    print(k2)
'''

# Task 2
'''
with open("2.txt") as file:
    a = file.readline()
    count = 1 # Гарантируется хотя бы 1 чередование XYZ
    maxx = 0
    for i in range(len(a) - 1):
        if a[i] != a[i + 1]:
            count += 1
            maxx = max(count, maxx)
        else: # символы совпали
            count = 1
    print(maxx)
'''

# Task 3
'''
with open("2.txt") as file:
    a = file.readline()
    count = 1
    maxx = 0
    for i in range(len(a) - 1):
        if a[i] <= a[i + 1]: # Алфавитный порядок не нарушается при повторении символа
            count += 1
            maxx = max(count, maxx)
        else:
            count = 1
    print(maxx)
'''

# Task 4
# Максимальное кол. идущих подряд чётных цифр
'''
with open("1.txt") as file:
    a = file.readline()
    count = 0
    maxx = 0
    for i in range(len(a)):
        if a[i] % 2 == 0:
            count += 1
            maxx = max(count, maxx)
        else:
            count = 0
    print(maxx)

# Альтернатива где задаёшь какие числа искать.
# with open("1.txt") as file:
#     a = file.readline()
#     count = 0
#     maxx = 0
#     ch = '02468'
#     for s in a:
#         if s in ch:
#             count += 1
#             maxx = max(count, maxx)
#         else:
#             count = 0
'''

# Task 5
# Макс. количество идущих постоянно чередующихся букв и цифр
'''
digit = '456'
alh = 'abc'

with open("1.txt") as file:
    a = file.readline()
    count = 0
    maxx = 0
    for i in range(len(a) - 1):
        if (a[i] in digit and a[i + 1] in alh) or (a[i] in alh and a[i + 1] in digit):
            count += 1
            maxx = max(count, maxx)
        else:
            count = 1
    print(maxx)
'''

# Task 6
'''
'''

