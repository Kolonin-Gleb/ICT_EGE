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
                if (y and not z and (not x or w)) == 1:
                    print(x, y, z, w)

# wzxy
'''

# Task 2
# Нужно правильно расставить приоритет операций?
# Почему такой объёмный вывод?
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                # (x /\ ¬y) \/ (y ≡ z) \/ w
                if ( (not y and x) or (y == z) or w) == 1:
                    print(x, y, z, w)
'''

# Task 3
# РЕШУ ЕГЭ solution 
# https://inf-ege.sdamgia.ru/problem?id=15939
# Говорят, что верный ответ wzyx. Но вывод приводится другой.
# Да и с Maximum-ом не совпадает!!!
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if (z and y) or ((x <= z) == (y <= w)) == 0:
                    print(x, y, z, w)
'''




