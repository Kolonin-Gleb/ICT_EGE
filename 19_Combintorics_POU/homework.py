# w W ц Ц

# Task 1
# Сколько существует шестнадцатеричных четырёхзначных чисел, в которых
# все цифры различны и => УНИКАЛЬНОСТЬ ЧИСЕЛ
# никакие две чётные или две нечётные цифры не стоят рядом? => ЧЕРЕДОВАНИЕ ЧЁТНЫЙ НЕЧЁТНЫЙ

# Task 1
'''
# https://labs-org.ru/ege-8-training-18/
from itertools import product
k = 0
for x in product('0123456789ABCDEF', repeat=4): 
    if int(x[0], 16) != 0 and len(set(x)) == len(x): # Проверка на уникальность всех чисел. # С нуля не может начинаться
        # Проверка условия чередования чётных и нечётных
        # 1ая и 3я цифры чётные, а 2ая и 4ая - нечётные
        if int(x[0], 16) % 2 == int(x[2], 16) % 2 == 0 and int(x[1], 16) % 2 == int(x[3], 16) % 2 == 1:
            k += 1
        # 1ая и 3я цифры нечётные, а 2ая и 4ая - чётные
        if int(x[0], 16) % 2 == int(x[2], 16) % 2 == 1 and int(x[1], 16) % 2 == int(x[3], 16) % 2 == 0:
            k += 1

print(k) # 5880
'''

# Task 2
'''
Каждая из других допустимых букв может встречаться в слове любое количество раз или не встречаться совсем.
Слово не должно начинаться с буквы Т и оканчиваться гласными буквами. 
Словом считается любая допустимая последовательность букв, не обязательно осмысленная.
Сколько существует таких слов, которые может написать Вася?
'''
# 6-ти буквенные слова
# П-И-Т-О-Н
# Н =< 1 раз
# Т - не 1ая буква
# И, О - не последние буквы
# Сколько слов можно составить?

'''
from itertools import product
k = 0
for x in product('ПИТОН', repeat=6):
    if x.count("Н") <= 1 and x[0] != 'Т':
        if x[-2] != 'И' and x[-2] != 'О':
                k += 1

print(k) # 4352

# https://test.tutoronline.ru/informatika-i-ikt/ege/theme/perebor-slov-i-sistemy-schisleniya/11180
from itertools import product
k = 0

for x in product("ПИТОН", repeat=6):
    if x[0] != 'Т' and x[-1] in "ПТН" and x.count("Н") <= 1:
        k += 1

print(k)
'''

# Task 3
# Определите количество пятизначных чисел, записанных в девятеричной системе счисления, 
# в записи которых ровно одна цифра 3, при этом никакая из цифр 5, 6, 7, 8 не стоит рядом с цифрой 3.
'''
from itertools import product

k = 0

for x in product('012345678', repeat=5):
    if x.count('3') == 1 and x[0] != '0': # Одна 3 и не начинается с 0
        index_3 = x.index('3')
        if index_3 == 0:
            if x[1] in '0124':
                k += 1
        elif index_3 == 4:
            if x[3] in '0124':
                k += 1
        else:
            if x[index_3 - 1] in '0124' and x[index_3 + 1] in '0124':
                k += 1

print(k)
'''

# Task 4 # Моё неверное решение
'''
from itertools import product
# Под каким номером в списке идёт первое слово, которое не содержит ни одной буквы И и не содержит букв А,
# стоящих рядом?
## А = 0
# Б = 1
## И = 2
# К = 3
# С = 4

for x in product('01234', repeat=5):
    if x.count("2") == 0:
        # Проверка, что нет стоящих рядом А
        flag = True # Флаг, что предположение верно

        prev_el = x[0]
        for el in x[1::]:
            if prev_el == el and el == '0':
                flag = False
                break
            else:
                prev_el = el 
        if flag:
            print(x)
            break

# ('0', '1', '0', '1', '0')
# ('А', 'Б', 'А', 'Б', 'А')

print(int('1010', 2)) # 10 => +1
'''

# Task 4 # Разбор верного решения
'''
from itertools import product
number = 0

for x in product('АБИКС', 5):
    number += 1 # 1ое слово = ААААА. 5 букв А

    if x.count("И") == 0:
        flag = False # Буквы А стоят рядом?

        for i in range(4):
            if x[i] == x[i + 1] == 'А': # Буквы А стоят рядом. Нарушение условия.
                flag = True
                break
            if flag == False: # Если условие не было нарушено
                print(number)
                break
'''

# Task 5 # 
# Определите в этом списке количество слов с чётными номерами,
# которые не начинаются с буквы Ж и 
# при этом содержат в своей записи не более одной буквы Ч.

# My solution. Why error?
'''
from itertools import product
count = 0
number = 0

for x in product('АЖИМНУЧ', 6):
    number += 1

    if number % 2 == 0:
        if x[0] != "Ж":
            count_che = 0
            for i in range(5):
                if x[i] == 'Ч':
                    count_che += 1
            if count_che <= 1:
                count += 1
print(count)
'''

# CHATGPT solution
'''
from itertools import product

letters = 'АЖИМНУЧ'
words_count = 0

for i, word in enumerate(product(letters, repeat=6), start=1):
    word_str = ''.join(word)
    # Проверяем условия: четный номер и не начинается с Ж, содержит не более одной буквы Ч
    if i % 2 == 0 and not word_str.startswith('Ж') and word_str.count('Ч') <= 1:
        words_count += 1

# 39528
print("Количество слов с четными номерами, не начинающихся с 'Ж' и содержащих не более одной 'Ч':", words_count)
'''

# Maximum solution
'''
from itertools import product
number = 0 # Переменная для номера слова
k = 0 # Счётчик слов

for x in product('АЖИМНУЧ', repeat=6):
    number += 1

    if x[0] != 'Ж' and x.count("Ч") <= 1 and number % 2 == 0:
        k += 1

print(k)
'''
