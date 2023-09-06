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
'''

print("x, y, z, w")

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ((x and not(y)) or (x == z) or not(w)) == 0: # Эквиваленция в python это ==
                    print(x, y, z, w)

# TODO: Почему-то я не смог решить!
# Попробовать решить на бумаге, через систему урванений
# yzwx
