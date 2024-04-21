# Task 3
'''
from fnmatch import *

for i in range(0, 10**9, 1097):
    if fnmatch(str(i), '3?5?24*9'):
        print(i, i//1097)
'''

# Task 1
'''
f = open('1.txt')
data = f.readline()
f.close()

cur_count = 1
max_count = 1

data = data.replace('NCT', '*').replace('CTN', '*')

for i in range(len(data) - 1):
    if data[i] == '*' and data[i + 1] == '*':
        cur_count += 1
    else:
        max_count = max(max_count, cur_count)
        cur_count = 1

# Для проверки случая, когда максимальная послед. будет последней и не оборвётся.
max_count = max(cur_count, max_count)

print(max_count)
'''

# Task 2
'''
f = open('2.txt')
data = f.readline()
f.close()


# Гласные   будут 1
data = data.replace('A', '1')
data = data.replace('O', '1')
# Согласные будут 0
data = data.replace('B', '0')
data = data.replace('C', '0')
data = data.replace('D', '0')

# Замена нужных последовательностей на *
data = data.replace('110', '*')

k = 0 # тек. макс.
m = 0 # глоб. макс
# print(data)

for sym in data:
    if sym == '*':
        k += 1
        m = max(m, k)
    else:
        k = 0

print(m)
'''
    
# Task 4
'''
'''

def find_boxes(documents):
    # Сортируем номера документов в порядке убывания
    documents.sort(reverse=True)
    
    # Находим наименьший номер документа в третьей коробке
    third_box_min = documents[2 * 50 - 1]
    
    # Определяем количество коробок
    boxes_count = (len(documents) + 49) // 50
    
    return third_box_min, boxes_count

# Чтение входных данных из файла
with open('4.txt', 'r') as file:
    n = int(file.readline().strip())
    documents = [int(file.readline().strip()) for _ in range(n)]

# Вызов функции и вывод результатов
third_box_min, boxes_count = find_boxes(documents)
print(third_box_min, boxes_count)
