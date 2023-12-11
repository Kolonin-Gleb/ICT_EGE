# Комбинаторика в Python
# Задание 8 в ЕГЭ = 30% решают
# w W ц Ц
'''
k = 0
s = 'БЕЛКА'
# Сколько буквенные слова, столько и иклов
for x in s:
    for y in s:
        for z in s:
            for w in s:
                word = x + y + z + w # Формируем слово с помощью конкатенаии строк.
                if word.count('Б') == 1: # Б встречается = 1 раз
                    k += 1 # увеличиваем счётчик

print(k)
'''

# Example 1
'''
from itertools import product
k = 0

for x in product('0123456789', repeat=4):
    print(x[-1])
'''

# Example 2
'''
# Определить количество 5ти значных чисел в 8 С.С. 
# В записи которых = 1 цифра 6, при этом никакая нечётная цифра не стоит рядом с цифрой 6.

from itertools import product
k = 0

for x in product('01234567', repeat=5):
    if x[0] != "0" and x.count("6") == 1:
        index_6 = x.index("6")
        if index_6 == 0:
            if int(x[1]) % 2 == 0:
                k += 1
        elif index_6 == 4:
            if int(x[3]) % 2 == 0:
                k += 1
        else:
            if int(x[index_6 - 1]) % 2 == 0 and int(x[index_6 + 1]) % 2 == 0:
                k += 1

print(k) # 2961
'''

# Task 3

# Определить количество 5ти значных чисел в 8 С.С. 
# В записи которых нет 1, 
# которых все цифры различны и никакие 2 чётные и нечётные цифры не стоит рядом?

# 1 Вариант решения
'''
from itertools import product
k = 0
for x in product('0234567', repeat=5): # Отсекаем 1 из набора
    if x[0] != 0 and len(set(x)) == len(x): # Проверка на уникальность всех чисел. # С нуля не может начинаться
        # Проверка условия чередования чётных и нечётных

        # Проверка, что начинается с чётного
        if int(x[0]) % 2 == int(x[2]) % 2 == int(x[4]) % 2 == 0 and int(x[1]) % 2 == int(x[3]) % 2 == 1:
            k += 1
        # Проверка, что начинается с нечётного
        if int(x[0]) % 2 == int(x[2]) % 2 == int(x[4]) % 2 == 1 and int(x[1]) % 2 == int(x[3]) % 2 == 0:
            k += 1

print(k) # 216
'''

# 2 Вариант решения
'''
from itertools import product
k = 0
for x in product('0234567', repeat=5): # Отсекаем 1 из набора
    if x[0] != 0 and len(set(x)) == len(x): # Проверка на уникальность всех чисел. # С нуля не может начинаться
        # Проверка условия чередования чётных и нечётных
        flag = True 
        for i in range(len(x) - 1): # Идём по индексам кортежа
            if int(x[i]) % 2 == int(x[i + 1]) % 2: # Нет чередования
                flag = False
        if flag == True:
            k += 1

print(k) # 216
'''

# Task 4
# 6ти буквенные слова из букв "М, А, Н, Г, У, С, Т"

'''
from itertools import product
k = 0 # Номер слова

for x in product("МАНГУСТ", repeat=6):
    k += 1
    if x[0] != "У" and x.count("М") == 2 and x.count("Г") <= 1:
        print(k) # 117601
'''

# Task 5

'''
from itertools import product
k = 0
number = 0

for x in product("АИНПТЦЯ", repeat=6):
    number += 1
    if x[0] != 'Н' and x.count("Я") == 2 and number % 2 == 0:
        k += 1

print(k) # 8640
'''

