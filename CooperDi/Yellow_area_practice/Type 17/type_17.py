# 8692

# Определить кол. пар последовательности,
# в которых только один из элементов является трехзначным числом
# а сумма элементов пары
# кратна максимальному трехзначному элементу последовательности.!!!!!!!!!!!

# В ответе запишите количество найденных пар,
# затем МАКСИМАЛЬНУЮ из сумм элементов таких пар.

# В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
'''
def is_3_digigit(n):
    if n > 99 and n < 1000:
        return True
    return False


f = open('17_8682.txt')
data = f.readlines()
f.close()

data = [int(i) for i in data]

max_3 = 0

for el in data:
    if el > 99 and el < 1000:
        max_3 = max(max_3, el)

pair_counter = 0
max_pair_sum = 0

for i in range(len(data) - 1):
    if (is_3_digigit(data[i]) and not is_3_digigit(data[i + 1])) or (is_3_digigit(data[i + 1]) and not is_3_digigit(data[i])):
        if (data[i] + data[i + 1]) % max_3 == 0:
            pair_counter += 1
            max_pair_sum = max(max_pair_sum, data[i] + data[i + 1])

print(pair_counter, max_pair_sum) # 502 461538
'''

# № 8427 (Уровень: Средний)

# Файл содержит последовательность натуральных чисел, не превышающих 20_000.
# Назовём парой два идущих подряд элемента последовательности.

# Определите количество пар, для которых выполняются следующие условия:
# – ровно одно число в паре четырёхзначное;
# – сумма квадратов элементов пары без остатка делится на наименьшее в последовательности трёхзначное число,
# запись которого заканчивается цифрой 3.

# В ответе запишите два числа: сначала количество найденных пар,
# затем максимальную из сумм квадратов элементов таких пар.
'''
def is_4_digigit(n):
    if n > 999 and n < 10_000:
        return True
    return False
def is_3_digigit(n):
    if n > 99 and n < 1000:
        return True
    return False

f = open('17_8427.txt')
data = f.readlines()
data = [int(i) for i in data]
f.close()

pair_counter = 0
max_squares_sum = 0
min_3_ends_3 = 999

for el in data:
    if is_3_digigit(el):
        if el % 10 == 3:
            min_3_ends_3 = min(min_3_ends_3, el)

for i in range(len(data) - 1):
    if ( (is_4_digigit(data[i]) and not is_4_digigit(data[i + 1])) or (is_4_digigit(data[i + 1]) and not is_4_digigit(data[i]))):
        if (data[i] ** 2 + data[i + 1] ** 2) % min_3_ends_3 == 0:
            pair_counter += 1
            max_squares_sum = max(max_squares_sum, data[i] ** 2 + data[i + 1] ** 2)

print(pair_counter, max_squares_sum) # 74 433966217
'''

	
# № 7596 Досрочная волна 2023 (Уровень: Базовый)
# В файле содержится последовательность целых чисел.
# Элементы последовательности могут принимать целые значения от 1 до 100 000 включительно.
# Определите количество пар последовательности, в которых
# только одно число трехзначное,
# и сумма элементов пары кратна минимальному трехзначному значению последовательности, оканчивающемуся на 5.
# 
# В ответе запишите два числа:
# сначала количество найденных пар,
# затем минимальную из сумм элементов таких пар.
'''
def is_3_digit(n):
    return 100 <= n <= 999

f = open("17_7596.txt")
data = [int(i) for i in f]
f.close()

min_3_ends_5 = min(el for el in data if el % 10 == 5 and is_3_digit(el))

pair_counter = 0
min_pair_sum = float('inf') # TODO: почему не работает с = 9999

for i in range(len(data) - 1):
    if (is_3_digit(data[i]) and not is_3_digit(data[i + 1])) or \
    (is_3_digit(data[i + 1]) and not is_3_digit(data[i])):
        if (data[i] + data[i + 1]) % min_3_ends_5 == 0:
            pair_counter += 1
            min_pair_sum = min(min_pair_sum, (data[i] + data[i + 1]))

print(pair_counter, min_pair_sum)
'''

