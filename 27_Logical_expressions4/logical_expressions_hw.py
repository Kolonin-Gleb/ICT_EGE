"""
for A in range(1, 10_000): # A - целое неотр. число
    if A % 100 == 0:
        print(f"progress = {A}")

    flag = True
    for x in range(1, 500):
        if ((x % A != 0) <= ((x % 6 == 0) <= (x % 21 != 0))) == 0: # Следует либо упростить формулу, либо расставить ()
            flag = False # Параметр не подошёл
            break
    if flag == True:
        print(A)
        # break # Т.к. просят найти наименьшее
"""

# Task 1
'''
for A in range(10_000):
    if A % 100 == 0:
        print(f"progress = {A}")

    flag = True
    for x in range(500):
        for y in range(500):
            if ((x * y > A) or (x > y) or (x <= 13)) == 0:
                flag = False
                break
    if flag == True:
        print(A)
        # break # Просят найти наибольшее
'''

# Task 2
"""
counter = 0
for A in range(10_000):
    if A % 100 == 0:
        print(f"progress = {A}")

    flag = True
    for x in range(500):
        for y in range(500):
            if ((x >= 9) <= (x**2 >= A)) and ((y**2 >= A) <= (y > 5)) == 0:
                flag = False
                break
    if flag == True:
        counter += 1
        # print(A)
        # break # Просят найти наибольшее

print(counter)
"""


count = 0
for a in range(1, 300):
    k = 0
    for x in range(0, 300):
        for y in range(0, 300):
            if ((x >= 9) <= (x**2 < a)) and ((y**2 >= a) <= (y > 5)):
                k += 1
    if k == 90_000:
        count += 1
print(count)



# Task 3
'''
P = list(range(3, 14))
Q = list(range(6, 21))

for A in range(1000):
    flag = True
    for x in range(500):
        if ((not(x in Q) <= (x in P)) <= (x in A)) == 0:
            flag = False
            break
    if flag:
        print(A)
        # Нужно будет посчитать длину отрезк Amax - Amin
'''

# 
