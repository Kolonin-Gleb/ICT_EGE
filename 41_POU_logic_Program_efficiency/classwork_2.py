# ПОУ Логика 2
# Книга курса 51


# Task 1
'''
print("x y z w")

for x in 0,1:
    for y in 0,1:
        for w in 0,1:
            for z in 0,1:
                if ((y <= x) or not (z <= w)) == 0:
                    print(x, y, z, w)
# zywx
'''

# Task 2
'''
print("x y z w")

for x in 0,1:
    for y in 0,1:
        for w in 0,1:
            for z in 0,1:
                if (x or not (w <= y) or (x == z)) == 0:
                    print(x, y, z, w)
'''

# Task 3
'''
for A in range(1000): # неотрицательные A
    flag = True # 
    for x in range(500):
        for y in range(500):
            if ( (y + 3*x != 60) or (x > A) or (y > A) ) == 0: # Сравниваем с противоположным значением
                flag = False
                break
    if flag:
        print(A) # 14
'''

# Task 4
'''
for A in range(1000): # неотрицательные A
    flag = True # 
    for x in range(1, 500):
        if ( (A + x > 75) or (x % 3 == 0) <=  (x % 7 != 0) ) == 0: # Сравниваем с противоположным значением
            flag = False
            break
    if flag:
        print(A) # 55
        break
'''

# Task 5
'''
for A in range(1000): # неотрицательные A
    flag = True # 
    for x in range(1, 500):
        if ( (A + x > 75) or (x % 3 == 0) <=  (x % 7 != 0) ) == 0: # Сравниваем с противоположным значением
            flag = False
            break
    if flag:
        print(A) # 55
        break
'''


