'''
'''
# Task 1
# Определите максимальное количество идущих подряд символов,
# среди которых каждые два соседних являются одинаковыми.
'''
with open("1.txt") as file:
    a = file.readline()
    k1 = 1
    maxx = 0
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            k1 += 1
            maxx = max(k1, maxx)
        else:
            k1 = 1
    print(maxx)
'''

# Task 2
'''
def max_non_decreasing_digits(text):
    max_count = 1  # Переменная для хранения максимальной длины последовательности цифр
    current_count = 1  # Переменная для хранения текущей длины последовательности цифр
    for i in range(len(text) - 1):
        # Если следующая цифра Меньше или равна текущей, увеличиваем счетчик
        if text[i] >= text[i + 1]:
            current_count += 1
        else:
            # Если последовательность закончилась, обновляем максимальное значение
            max_count = max(max_count, current_count)
            current_count = 1  # Сбрасываем счетчик
    # Обновляем максимальное значение после прохода по всему тексту
    max_count = max(max_count, current_count)
    return max_count

# Пример использования функции
with open("2.txt") as file:
    text = file.readline()
    print("Максимальное количество идущих подряд цифр, расположенных в порядке невозрастания:", 
    max_non_decreasing_digits(text))
'''

# Task 3
'''
with open("3.txt") as file:
    a = file.readline()
    count = 0
    maxx = 0
    for i in range(len(a)):
        if int(a[i]) % 3 != 0:
            count += 1
            maxx = max(count, maxx)
        else:
            count = 0
    print(maxx)
'''

# Task 4
'''
with open("4.txt") as file:
    a = file.readline()
    count = 0
    maxx = 0
    ch = 'STLKR'

    for s in a:
        if s in ch:
            count += 1
            maxx = max(count, maxx)
        else:
            count = 0
    print(maxx)
'''

# Task 5
f = open('5.txt')
a = f.readline()
cur_l, max_l = 0, 0

for i in range(len(a)-2):
    if a[i] != a[i + 1] and a[i] == a[i + 2]:
        cur_l += 1
        max_l = max(cur_l + 2, max_l)
    else:
        cur_l = 0

print(max_l)
f.close()
