# 189
'''
Вася составляет 6-буквенные слова, в которых есть только буквы К, Р, О, Т,
причём буква О используется в каждом слове ровно 1 раз.

Каждая из других допустимых букв может встречаться в слове любое количество раз или не встречаться совсем.
Словом считается любая допустимая последовательность букв, не обязательно осмысленная.
Сколько существует таких слов, которые может написать Вася?
'''

"""
count = 0
for b1 in 'КРОТ':
    for b2 in 'КРОТ':
        for b3 in 'КРОТ':
            for b4 in 'КРОТ':
                for b5 in 'КРОТ':
                    for b6 in 'КРОТ':
                        s = b1+b2+b3+b4+b5+b6
                        if s.count('О') == 1: # О - (обязательно присутствует?) и лишь 1 раз # Может ли быть слово вообще без О?
                            count += 1
print(count) # 1458
"""

# 196
# Й - согласный!!!
'''
count = 0
for b1 in 'БЕРКЛИ':
    for b2 in 'БЕРКЛИЙ':
        for b3 in 'БЕРКЛИЙ':
            for b4 in 'БЕРКЛИЙ':
                s = b1+b2+b3+b4
                if 'Е' in s or 'И' in s:
                     count += 1
print(count) # 1558
'''

# 201
'''
count = 0
for b1 in 'ПЕСКАР': # Без Ь
    for b2 in 'ПЕСКАРЬ':
        for b3 in 'ПЕСКАРЬ':
            for b4 in 'ПЕСКАРЬ':
                for b5 in 'ПЕСКАРЬ':
                    for b6 in 'ПЕСКАРЬ':
                        for b7 in 'ПЕСКАРЬ':
                            s = b1+b2+b3+b4+b5+b6+b7
                            if not ('ЬЕ' in s or 'ЬА' in s or 'ЬР' in s):
                                # Каждую букву из набора размера 7 можно использовать лишь 1 раз => все буквы присутствуют
                                if 'П' in s and 'Е' in s and 'С' in s and 'К' in s and 'А' in s and 'Р' in s and 'Ь' in s:
                                    count += 1

print(count) # 2520
'''

# 399
# TODO: Ответ не совпадает выводит 288.
'''
count = 0

for b1 in "ВОРОТА":
    for b2 in "ВОРОТА":
        for b3 in "ВОРОТА":
            for b4 in "ВОРОТА":
                for b5 in "ВОРОТА":
                    for b6 in "ВОРОТА":
                        s = b1+b2+b3+b4+b5+b6
                        # Проверка, что образованно перестановкой
                        if s.count("О") == 2 and 'В' in s and 'Р' in s and "Т" in s and "А" in s:
                            if not('ОО' in s or "ОА" in s or "АО" in s):
                                count += 1

print(count)
'''

# 399 Attempt 2 using itertools
'''
from itertools import permutations

count = 0
for i in set(permutations("ВОРОТА", r=6)): # Добавив set() -- исключается дублирование букв
    s = ''.join(i)
    if not('ОО' in s or "ОА" in s or "АО" in s):
        count += 1
    # if s.count("О") == 2: # Проверка, что в словах может быть 2 буквы О
        # print(s)

print(count)
'''

# 4957
# TODO: Почему не удалось разделить на 2 условия?
'''
from itertools import permutations, product

glasnie = [''.join(x) for x in product('АИЯ', repeat = 3)]   # Все возможные комбинации 3х указанных гласных
soglasnie = [''.join(x) for x in product('НСТ', repeat = 3)] # Все возможные комбинации 3х указанных согласных

count = 0

for i in set(permutations("АНАСТАСИЯ", r=9)):
    s  = ''.join(i)
    if not(any( (comb_g in s) for comb_g in glasnie) and any( (comb_s in s) for comb_s in soglasnie)):       # Проверка, что в слове нет ни одной комбинации 3х подряд гласных
        # if not(any( (comb_s in s) for comb_s in soglasnie)): # Проверка, что в слове нет ни одной комбинации 3х подряд согласных
            # count += 1
        count += 1

print(count) # 23040
'''

# 3028
'''
# 7 циклов. 9 С.С. => 012345678
count = 0
for d1 in '124568':
    for d2 in '012345678':
        for d3 in '012345678':
            for d4 in '012345678':
                for d5 in '012345678':
                    for d6 in '012345678':
                        for d7 in '012345678':
                            # Не должно быть пар соседних одинаковых чисел
                            s = d1+d2+d3+d4+d5+d6+d7
                            flag = True
                            for i in range(len(s) - 1):
                                if s[i] == s[i+1]:
                                    flag = False # Условие отсутствия соседних пар одинаковых чисел нарушено
                                    break
                            if flag:
                                count += 1
print(count) # 1572864 - correct! =)
'''

# 4613
'''
# 5 циклов. 9 С.С. => 012345678
# не начинаются с нечетных цифр, +
# не оканчиваются цифрами 1 или 8, +
# а также содержат в своей записи не более одной цифры 3. +

count = 0
for d1 in '2468': # без 0 и нечётных
    for d2 in '012345678':
        for d3 in '012345678':
            for d4 in '012345678':
                for d5 in '0234567': # без 1 и 8
                    s = d1+d2+d3+d4+d5
                    if s.count('3') <= 1: # не более 1 цифры 3
                        count += 1

print(count) # 18944
'''

# 4696
# TODO: Может немного костыль, но сделал сам
'''
# 5 циклов. 8 С.С. => 01234567
# в записи которых только одна цифра 6,
# при этом никакая нечётная цифра не стоит рядом с цифрой 6.

count = 0
for d1 in '1234567': # без 0
    for d2 in '01234567':
        for d3 in '01234567':
            for d4 in '01234567':
                for d5 in '01234567':
                    s = d1+d2+d3+d4+d5
                    if s.count('6') == 1: # = 1 цифра 6
                        # нет нечётных рядом с цифрой 6

                        # Проверка, что 6 на 1ой или последней позиции
                        if (s.find('6') == 4 and s[3] not in '1357') or (s.find('6') == 0 and s[1] not in '1357'):
                            count += 1
                        # Проверка, когда 6 посередине
                        elif s[s.find('6') - 1] not in '1357' and s[s.find('6') + 1] not in '1357':
                            count += 1

print(count) # 2961
'''

# 6892
# TODO: Может немного костыль, но сделал сам
# 6 Циклов. 6 С.С. => 012345 +
# = одна цифра 2 +
# никакая ничётная цифра не стоит рядом с цифрой 2 +
'''
count = 0
for d1 in '12345': # без 0
    for d2 in '012345':
        for d3 in '012345':
            for d4 in '012345':
                for d5 in '012345':
                    for d6 in '012345':
                        s = d1+d2+d3+d4+d5+d6
                        if s.count('2') == 1: # = одна цифра 2
                            # нет нечётных рядом с цифрой 2

                            # Проверка, что 2 на 1ой или последней позиции
                            if (s.find('2') == 5 and s[4] not in '135') or (s.find('2') == 0 and s[1] not in '135'):
                                count += 1
                            # Проверка, когда 2 посередине
                            elif s[s.find('2') - 1] not in '135' and s[s.find('2') + 1] not in '135':
                                count += 1

print(count)
'''

# 1927
'''
count = 0

for b1 in 'СНВДЦ': # Согласные
    for b2 in 'ЯСНОВИДЕЦ':
        for b3 in 'ЯСНОВИДЕЦ':
            for b4 in 'ЯСНОВИДЕЦ':
                for b5 in 'ЯОИЕ': # Гласные
                    s = b1+b2+b3+b4+b5
                    if s.count(b1) == 1 and s.count(b5) == 1:
                        count += 1

print(count) # 6860
'''

# 9773 
'''
'''

