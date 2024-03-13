# type 2 practice screenshot 1
'''
print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (x or y) and (not(y == z)) and (not(w)) == 1:
                    print(x, y, z, w)
# z y x w
'''

# Task 1
'''
x y z w
0 0 0 1
0 0 1 0
0 1 0 1
0 1 1 1
'''

# Task 2
'''
x y z w
1 0 0 0
1 0 1 0
1 1 1 0
'''
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ( (x <= (y and (not z)) ) or w) == 0: # ВНИМАТЕЛЬНО РАССТАВИТЬ СКОБКИ, В СООТВЕТСТВИИ С ПРИОРИТЕТОМ!
                    print(x, y, z, w)
'''

# Type 8 task 1
'''
count = 0
for b1 in 'КМТ':
    for b2 in 'ОЕА':
        for b3 in 'КМТ':
            for b4 in 'ОЕА':
                for b5 in 'КМТ':
                    for b6 in 'ОЕА':
                        slovo = b1+b2+b3+b4+b5+b6
                        if slovo.count("К") == 1 and slovo.count("М") == 1 and slovo.count("Т") == 1 \
                            and slovo.count("О") == 1 and slovo.count("Е") == 1 and slovo.count("А") == 1:
                            count += 1


for b1 in 'ОЕА':
    for b2 in 'КМТ':
        for b3 in 'ОЕА':
            for b4 in 'КМТ':
                for b5 in 'ОЕА':
                    for b6 in 'КМТ':
                        slovo = b1+b2+b3+b4+b5+b6
                        if slovo.count("К") == 1 and slovo.count("М") == 1 and slovo.count("Т") == 1 \
                            and slovo.count("О") == 1 and slovo.count("Е") == 1 and slovo.count("А") == 1:
                            count += 1

print(count) # 72
'''

# Type 8 task 2
# ПОВТОРЯЮЩИЕСЯ БУКВЫ НУЖНО УБРАТЬ ПРИ ПЕРЕБОРЕ,
# т.к. имеем дело с перестановками.
# и можно собрать одно и тоже слово несколько раз (при наличии повт. букв)
'''
count = 0
for b1 in 'БИТКОН':
    for b2 in 'БИТКОН':
        for b3 in 'БИТКОН':
            for b4 in 'БИТКОН':
                for b5 in 'БИТКОН':
                    for b6 in 'БИТКОН':
                        for b7 in 'БИТКОН':
                            slovo = b1+b2+b3+b4+b5+b6+b7
                            if slovo.count("И") == 2 and slovo.count("Б") == 1 and slovo.count("Т") == 1 \
                                and slovo.count("К") == 1 and slovo.count("О") == 1 and slovo.count("Н") == 1:
                                count += 1

print(count) # 2520
'''

# Type 8 task 3
'''
count = 0
for b1 in 'ЗАПИС': # без Ь
    for b2 in 'ЗАПИСЬ':
        for b3 in 'ЗАПИСЬ':
            for b4 in 'ЗАПИСЬ':
                for b5 in 'ЗАПИСЬ':
                    for b6 in 'ЗАПИСЬ':
                        slovo = b1+b2+b3+b4+b5+b6
                        if slovo.count("З") == 1 and slovo.count("А") == 1 and slovo.count("П") == 1 \
                            and slovo.count("И") == 1 and slovo.count("С") == 1 and slovo.count("Ь") == 1:
                            if 'АЬ' not in slovo and 'ИЬ' not in slovo:
                                count += 1

print(count) # 360
'''

# Type 8 task 4
'''
'''
# 6-ти значные
# 5 ричная С.С. # 01234
'''
count = 0
for b1 in '234':
    for b2 in '01234':
        for b3 in '01234':
            for b4 in '01234':
                for b5 in '01234':
                    for b6 in '012':
                        count += 1

print(count)
'''

# Type 8 task 5
'''
'''

# 7 циклов
# 0123456 (7 C.С.)
'''
count = 0 

for b1 in '1246':
    for b2 in '0123456':
        for b3 in '0123456':
            for b4 in '0123456':
                for b5 in '0123456':
                    for b6 in '0123456':
                        for b7 in '0123456':
                            s = b1+b2+b3+b4+b5+b6+b7
                            if ('22' in s and '44' in s) == 0:
                                count += 1

print(count) # 466456
'''

