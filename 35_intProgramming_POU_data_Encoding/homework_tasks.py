# Example
# Найти количество пар и Максимальное произведение
'''
f = open('***.txt') # открываем текстовый файл с режиме чтения

a = [int(i) for i in f] # сохраняем все числа из текстового файла в список

k = 0# переменная-счетчик количества найденных пар чисел
m = 0# переменная для хранения максимального произведения

for i in range(len(a) - 1): # проходимся вдоль списка для анализа каждой пары чисел
    if a[i] % 5 == 0 or a[i + 1] % 5 == 0: # проверка, что хотя бы одно число пары делится на 5
        k += 1 # увеличиваем счетчик найденных пар на 1
    m = max(m, a[i] * a[i + 1]) # ищем максимальное произведение пары

print(k, m) # выводим ответ на экран
f.close()# закрываем файл
'''

# Task 1
# количество пар элементов последовательности, в которых оба числа делятся на 3,
# затем максимальную из сумм элементов таких пар
'''
with open('1.txt') as file:
    data = [int(i) for i in file]

    k = 0 # Количество пар
    s = -9999999999999999999 # максимальная сумма

    for i in range(len(data) - 1):
        if data[i] % 3 == 0 and data[i + 1] % 3 == 0:
            k += 1
            s = max(s, data[i] + data[i + 1])
        
    print(k, s)
'''

# Task 2
# количество пар элементов последовательности, в которых хотя бы одно число делится на 13, 
# затем минимальную из сумм элементов таких пар
'''
with open('2.txt') as file:
    data = [int(i) for i in file]

    k = 0
    s = 999999999999999999999999

    for i in range(len(data) - 1):
        if data[i] % 13 == 0 or data[i + 1] % 13 == 0:
            k += 1
            s = min(s, data[i] + data[i + 1])
    
    print(k, s)
'''

# Task 3
# количество пар элементов последовательности, в которых одно число оканчивается на 5, а другое на 3 (порядок не важен),
# затем минимальное из произведений элементов таких пар.
'''
with open('3.txt') as file:
    data = [int(i) for i in file]

    k = 0
    m = 9999999999999999999

    for i in range(len(data) - 1):
        if (data[i] % 10 == 5 and data[i + 1] % 10 == 3) or (data[i + 1] % 10 == 5 and data[i] % 10 == 3):
            k += 1
            m = min(m, data[i] * data[i + 1])

    print(k, m)
'''

# Task 4
# количество пар элементов последовательности, в которых ровно одно число оканчивается на ту же цифру,
# что и максимальный четный элемент в последовательности, затем максимальное из произведений элементов таких пар.
'''
with open('4.txt') as file:
    data = [int(i) for i in file]

    max_even_el = -10_001
    for el in data:
        if el % 2 == 0:
            max_even_el = max(max_even_el, el)

    max_even_el_last_digit = max_even_el % 10

    k = 0
    m = -9999999999999999

    for i in range(len(data) - 1):
        if (data[i] % 10 == max_even_el_last_digit and data[i + 1] % 10 != max_even_el_last_digit) or (data[i] % 10 != max_even_el_last_digit and data[i + 1] % 10 == max_even_el_last_digit):
            k += 1
            m = max(m, data[i] * data[i + 1])

    print(k, m)
''' 

# Task 5
# количество пар элементов последовательности, в которых оба числа не делятся на
# минимальный по модулю элемент последовательности, кратный 13.
# В ответе запишите количество найденных пар, затем минимальную из сумм элементов таких пар
'''
with open('5.txt') as file:
    data = [int(i) for i in file]

    min_13 = 99999999
    for el in data:
        if abs(el) % 13 == 0:
            min_13 = min(min_13, el)
    
    k = 0
    s = 9999999999
    for i in range(len(data) - 1):
        if ((data[i] % min_13 != 0) and (data[i + 1] % min_13 != 0)):
            k += 1
            s = min(s, data[i] + data[i + 1])
    
    print(k, s)
'''

# Task 6
# количество пар элементов последовательности, в которых хотя бы один элемент оканчивается на 9,
# а сумма элементов пары меньше, чем максимальный элемент последовательности, кратный 15.
'''
with open('6.txt') as file:
    data = [int(i) for i in file]

    max_15 = 0
    for el in data:
        if el % 15 == 0:
            max_15 = max(max_15, el)

    k = 0
    s = -999999999999999999999999

    for i in range(len(data) - 1):
        if data[i] % 10 == 9 or data[i + 1] % 10 == 9:
            if data[i] + data[i + 1] < max_15:
                k += 1
                s = max(s, data[i] + data[i + 1])

    print(k, s)
'''

# Task 7
# Количество троек элементов последовательности, в которых все элементы кратны 3, 
# а
# сумма элементов тройки не более, чем максимальный элемент последовательности, оканчивающийся на 7.
# В ответе запишите количество найденных троек, затем минимальную по модулю сумму элементов таких троек.
'''
with open('7.txt') as file:
    data = [int(i) for i in file]

    max_7 = 0
    for el in data:
        if el % 10 == 7:
            max_7 = max(max_7, el)

    k = 0
    s = 99999999999999
    for i in range(len(data) - 2):
        if data[i] % 3 == 0 and data[i + 1] % 3 == 0 and data[i + 2] % 3 == 0:
            if (data[i] + data[i + 1] + data[i + 2]) <= max_7:
                k += 1
                s = min(s, abs(data[i] + data[i + 1] + data[i + 2]))

    print(k , s)
'''

# Task 8
# Определите количество троек последовательности, в которых ни одно из чисел не кратно 6,
# а сумма элементов тройки не менее, чем максимальный элемент последовательности, оканчивающийся на 4.
# В ответе запишите количество найденных троек, затем абсолютное значение минимальной из сумм элементов таких троек.
'''
with open('8.txt') as file:
    data = [int(i) for i in file]

    max_4 = 0

    for el in data:
        if el % 10 == 4:
            max_4 = max(max_4, el)

    k = 0
    s = 9999999999999999999

    for i in range(len(data) - 2):
        if data[i] % 6 != 0 and data[i + 1] % 6 != 0 and data[i + 2] % 6 != 0:
            if data[i] + data[i + 1] + data[i + 2] >= max_4:
                k += 1
                s = min(s, abs(data[i] + data[i + 1] + data[i + 2]))

    print(k, s)
'''

# Task 9
# Определите количество троек последовательности, в которых только одно число оканчивается на ту же цифру,
# что и максимальный элемент последовательности, кратный 3.
# В ответе запишите количество найденных троек, затем минимальную сумму элементов тройки. 
'''
with open('9.txt') as file:
    data = [int(i) for i in file]

    max_3 = 0

    for el in data:
        if el % 3 == 0:
            max_3 = max(max_3, el)

    max_3_last_dig = max_3 % 10
    k = 0
    s = 99999999999999999
    
    for i in range(len(data) - 2):
        if (data[i] % 10 == max_3_last_dig and data[i + 1] % 10 != max_3_last_dig and data[i + 2] % 10 != max_3_last_dig) or (data[i] % 10 != max_3_last_dig and data[i + 1] % 10 == max_3_last_dig and data[i + 2] % 10 != max_3_last_dig) or (data[i] % 10 != max_3_last_dig and data[i + 1] % 10 != max_3_last_dig and data[i + 2] % 10 == max_3_last_dig):
            k += 1
            s = min(s, (data[i] + data[i + 1] + data[i + 2]))

    print(k , s)
'''
