# 15314
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ((x and (not z)) or (y == z) or (not w)) == 0:
                    print(x, y, z, w)
'''
"""
x y z w
0 0 1 1
0 1 0 1
1 0 1 1
"""
# wyzx

# 10084
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
            # F=    (x  ∧   ¬   y)   ∨ (y ≡  z)  ∨    ¬w
                if ((x and (not y)) or (y == z) or (not w)) == 0:
                    print(x, y, z, w)
'''
"""
x y z w
0 0 1 1
0 1 0 1
1 1 0 1
"""
# wzyx

# 6843 - Авторская задача с уникальной таблицей истинности (F = 1 и = 0)
# СКИПАЙ ТАКУЮ ЗАДАЧУ
# Не знаю как решать.
'''
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                #    (𝑧→𝑤)     ∧𝑦   ∧    ¬𝑥
                if ( (z <= w) and y and (not x) ) == 0:
                    print(x, y, z, w)
""" Для F = 1
x y z w
0 1 0 0
0 1 0 1
0 1 1 1
"""
""" Для F = 0
x y z w
0 0 0 0
0 0 0 1
0 0 1 0
0 0 1 1
0 1 1 0
1 0 0 0
1 0 0 1
1 0 1 0
1 0 1 1
1 1 0 0
1 1 0 1
1 1 1 0
1 1 1 1
"""

# 1888
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ( (not x) or z or (not w) and y ) == 0:
                    print(x, y, z, w)
                    
'''
# yxwz
"""
x y z w
1 0 0 0
1 0 0 1
1 1 0 1
"""
# =================== Type 5 ===================
'''
lst = []
for N in range(1, 10_001):
    N_2 = bin(N)[2:]
    R_2 = ''
    if N % 2 == 0:
        R_2 = N_2 + "01"
    else:
        R_2 = '1' + N_2 + '1'
    
    R = int(R_2, 2)
    if R > 156:
        lst.append(N)

print(min(lst)) # 33
'''

# 4610
'''
lst = []
for N in range(1, 10_001):
    N_2 = bin(N)[2:]
    R_2 = ''
    if N_2.count('1') % 2 == 0:
        R_2 = '10' + N_2[2:] + '0'
    else:
        R_2 = '11' + N_2[2:] + '1'
    
    R = int(R_2, 2)
    if R < 35:
        print(N) # Максимальное = последнее
        # 24
'''

# 9736
'''
lst = []
for N in range(1, 10_001):
    N_2 = bin(N)[2:]
    R_2 = ''
    if N % 3 == 0:
        R_2 = N_2 + N_2[-3:]
    else:
        ost = (N % 3) * 3
        R_2 = N_2 + bin(ost)[2:]
    
    R = int(R_2, 2)
    if R <= 170:
        lst.append(R)

print(max(lst)) # 166
'''

# 9828
'''
def dec_to_3(n):
    res = ''
    while n > 0:
        res = str(n % 3) + res
        n //= 3
    return res

lst = []
for N in range(1, 10_001):
    N_3 = dec_to_3(N)
    R_3 = ''
    if N % 3 == 0:
        R_3 = '1' + N_3 + '02'
    else:
        ost = dec_to_3((N%3)*4)
        R_3 = N_3 + ost
    R = int(R_3, 3)
    # for tests
    # print(R_3)
    # print(R)
    if R < 199:
        print(N) # 20
'''

# =================== Type 8 # Combinatorics ===================

# 196
'''
vowels = 'ЕИ' # Й - согласная буква
counter = 0
for b1 in "БЕРКЛИ":
    for b2 in "БЕРКЛИЙ":
        for b3 in "БЕРКЛИЙ":
            for b4 in "БЕРКЛИЙ":
                word = b1+b2+b3+b4
                if word.count('Е') + word.count('И') > 0:
                    counter += 1
print(counter) # 1558
'''

# 200
'''
counter = 0
for b1 in 'КОМЕТА':
    for b2 in 'КОМЕТА':
        for b3 in 'КОМЕТА':
            for b4 in 'КОМЕТА':
                for b5 in 'КОМЕТА':
                    for b6 in 'КОМЕТА':
                        word = b1+b2+b3+b4+b5+b6
                        if len(set(word)) == 6:
                            word = word.replace('К', '*').replace('М', '*').replace('Т', '*')
                            word = word.replace('О', '-').replace('Е', '-').replace('А', '-')
                            if word.count('**') == 0 and word.count('--') == 0:
                                counter += 1
print(counter) #72
'''

# 399
'''
# ВАЖНО: В слове буквы которого переставляются имеется повторяющаяся буква!!
# Для решения проблемы подсчёта следует использовать set()
counter = 0
for b1 in set("ВОРОТА"):
    for b2 in set("ВОРОТА"):
        for b3 in set("ВОРОТА"):
            for b4 in set("ВОРОТА"):
                for b5 in set("ВОРОТА"):
                    for b6 in set("ВОРОТА"):
                        word = b1+b2+b3+b4+b5+b6
                        # Т.к. идёт перестановка букв кол. букв каждого типа должно остаться прежним
                        if word.count("В") == 1 and word.count("О") == 2 and word.count("Р") == 1 and word.count("Т") == 1 and word.count("А") == 1:
                            # Чтобы не забыть какие-то сочетания, лучше заменить все гласные на *
                            word = word.replace("О", "*").replace("А", "*")
                            if word.count("**") == 0:
                                counter += 1
print(counter) # 72
'''

# 9831
'''
counter = 0
for d1 in '123456789ABCDEF': # Не забывать, что число с 0 не начинается!
    for d2 in '0123456789ABCDEF':
        for d3 in '0123456789ABCDEF':
            num = d1+d2+d3
            # ЧИСЛА ДОЛЖНЫ БЫТЬ РАЗЛИЧНЫ!
            if len(set(num)) == 3:
                num = num.replace('0', 'e').replace('2', 'e').replace('4', 'e').replace('6', 'e').replace('8', 'e').replace('A', 'e').replace('C', 'e').replace('E', 'e')
                num = num.replace('1', 'o').replace('3', 'o').replace('5', 'o').replace('7', 'o').replace('9', 'o').replace('B', 'o').replace('D', 'o').replace('F', 'o')
                if num.count('ee') == 0  and num.count('oo') == 0:
                    counter += 1
print(counter) # 840
'''

# 4613
'''
counter = 0
for d1 in '12345678':
    for d2 in '012345678':
        for d3 in '012345678':
            for d4 in '012345678':
                for d5 in '012345678':
                    num = d1+d2+d3+d4+d5
                    if num[-1] != '1' and num[-1] != '8' and num.count('3') <= 1:
                        if num[0] != '1' and num[0] != '3' and num[0] != '5' and num[0] != '7' and num[0] != '9':
                            counter += 1
print(counter) #18944
'''

# 9739
'''
num = 0
for b1 in sorted("МАНГУСТ"):
    for b2 in sorted("МАНГУСТ"):
        for b3 in sorted("МАНГУСТ"):
            for b4 in sorted("МАНГУСТ"):
                for b5 in sorted("МАНГУСТ"):
                    for b6 in sorted("МАНГУСТ"):
                        num += 1
                        word = b1+b2+b3+b4+b5+b6
                        if b1 != 'У' and word.count("М") == 2 and word.count("Г") <= 1:
                            print(num, word) # 100810
'''

# 9777
'''
num = 0
for b1 in sorted("КОМПЬЮТЕР"):
    for b2 in sorted("КОМПЬЮТЕР"):
        for b3 in sorted("КОМПЬЮТЕР"):
            for b4 in sorted("КОМПЬЮТЕР"):
                for b5 in sorted("КОМПЬЮТЕР"):
                    num += 1
                    word = b1+b2+b3+b4+b5
                    if b1 != "Ь" and word.count('К') == 2:
                        print(num, word) # 58979 - нечётный!
'''
