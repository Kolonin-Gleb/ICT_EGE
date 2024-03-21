# Полезные ссылки с объяснениями:
# https://code-enjoy.ru/ege_po_informatike_2022_zadanie_2_ay_da_python/
# https://egogo.onrender.com/task/2

# Task 1
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if (y and not z and (not x or w)) == 1: # y /\ ¬z /\ (¬x \/ w)
                    print(x, y, z, w)

# wzxy
'''

# Task 2
# Нужно правильно расставить приоритет операций?
# (NOT Y) -- Обарачивай в ()
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                # (x /\ ¬y) \/ (y ≡ z) \/ w
                if ( ( (not y) and x) or (y == z) or w) == 0:
                    print(x, y, z, w)
# wzyx
'''

# Task 3
# Будет 1 лишняя строка, от которой легко избавиться
'''
'''

'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ( (z and y) or ((x <= z) == (y <= w)) ) == 0: # (z /\ y) \/ ((x → z) ≡ (y → w)
                    print(x, y, z, w)

# ywzx
'''

# Task 4
# Для какого НАИБОЛЬШЕГО целого числа А формула:
# (5y + x > A) \/ (y < 10) \/ (x ≤ 36)
# тождественно истинна, то есть принимает значение 1 при любых целых неотрицательных x и y?

'''
for A in range(1_000):

    flag = True # Условие что подходит
    for x in range(500):
        for y in range(500):
            if ( (5*y + x > A) or (y < 10) or (x <= 36) ) == 0: # Проверка на противоположное значение. Что неподходит
                flag = False
                break
    if flag == True:
        print(A) # 86
        # no break. Because looking for max
'''

# Task 5
# Для какого наименьшего целого числа А формула:
# (2x + 3y = 30) /\ (x ≥ y) /\ (y ≥ A)
# тождественно ложна, то есть принимает значение 0 при любых целых неотрицательных x и y?
'''
for A in range(1_000):
    flag = True # Условие что подходит
    for x in range(500):
        for y in range(500):
            if ( (2*x + 3*y == 30) and (x >= y) and (y >= A) ) == 1: # Проверка на противоположное значение
                flag = False
                break # Заход на новую итерацию с x
    if flag == True:
        print(A)
        break # to get min A
'''
