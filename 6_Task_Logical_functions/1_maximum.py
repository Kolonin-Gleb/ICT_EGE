# Task 1
'''
print("x, y, z") # Переменные из лог. функции

# Перебор всех возможных состояний переменных
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            if (x and y and not(z)) or (x and y and z) or (x and not(y) and not(z)) == 1: # Сравнение с лог. фукцией
                print(x, y, z)
# yxz
'''

# Task 2
'''
print("x, y, z, w")

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if y and not(z) and (not(x) or w) == 1:
                    print(x, y, z, w)
# yxzw
'''

# Task 3
'''
print("x, y, z, w")

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if (not(x) and y and z and not(w)) or (not(x) and y and not(z) and not(w)) or (x and y and z and not(w)) == 1:
                    print(x, y, z, w)
# zxwy
'''

# Task 4
'''
print("x, y, z, w")

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ((x and y and not(z) and not(w)) or (x and y and z and not(w)) or (x and not(y) and not(z) and not(w))) == 1:
                    print(x, y, z, w)
# zyxw
'''

# Task 5
'''
print("x, y, z, w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ((x and not(y)) or (x == z) or not(w)) == 0: # Эквиваленция в python это ==
                    print(x, y, z, w)
'''


# Коварная задачка.
# 1. Написать код для решения
# 2. Постараться заполнить пропущенные ячейки, где это очевидно из функции
# 3. Анализировать скобки с тождеством, для определения какие пары столбцов могут быть x и z
# 4. Используя вывод кода, дозаполнить пустые ячейки
# 5. Выполнить последний логический анализ, попробовав присвоить парам столбцов x и z поочередно,
# Убеждаясь в каком случае результат операции в () будет = 0
# 6. Записать ответ: yzwx

# Task 7 TODO: Почему выдаёт 6 строк, а не 3?
'''
'''
print("x, y, z, w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ( (z and y) or ((x <= y) == (y <= w)) ) == 0:
                    print(x, y, z, w)


print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not( (z and y) or ((x <= z) == (y <= w))):
                    print(x, y, z, w)

# Task 8
# F = (x ∨ y) → (z ≡ x) = 0
'''
print("x, y, z")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            if ((x or y) <= (z == x)) == 0:
                print(x, y, z)
'''

# Task 9
# F = (¬x ∧ ¬y) ∨ (y ≡ z) ∨ w = 0
'''
print("x, y, z, w")

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ( (not(x) and not(y)) or (y==z) or w) == 0:
                    print(x, y, z, w)
'''

