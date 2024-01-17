# Task 1
# F = z and not(x) and (w or not(z))
'''
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if (z and not(x) and (w or not(z))) == 1:
                    print(x, y, z, w)
# xzyw - ?
# Почему в ответ вышло всего 2 строки для сопоставления, а не 3?
'''

# Task 2
# (¬y \/ ¬x) /\ ¬(x ≡ z) /\ w
# Чтобы правильно сопоставить столбцы, следует упростить эту функцию!
print('x y z w')
for x in 0, 1:
    for y in 0, 1:
            for w in 0, 1:
                if ( (not(y) or not(x)) and not(x == z) and w) == 1:
                    print(x, y, z, w)
# Пусть будет
# xwzy

# Task 3
'''32'''

# Task 4
'''20'''

# Task 5
# Неуспел дописать
'''
for n in range(1, 100):
    s = bin(n)[2:]  # перевод в двоичную систему
    s = str(s) 
    if s[-1] == '0':
        s = '11' + s
    else:
        s = '1' + s + '00'
    r = int(s, 2)  # перевод в десятичную систему
    if r > 52:
        print(n)
        break
'''
