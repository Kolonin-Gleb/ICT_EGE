# Типовое задание 24
# Task 1
'''
f = open('1.txt')
a = f.readline()
maxx = 1 # Найденное максимальное кол. идущих подряд символов (не содержащих GIH)
count = 1 # Локальный максимум

for i in range(len(a) - 1):
    # Подход от обратного. Находим неподходящие последовательности
    if a[i] in 'GIH' and a[i + 1] in "GIH":
        # Данный вариант не подходит оставляем 1
        count = 1 # Именно 1, а не 0, т.к. рассматриваются пары и индексация начинается с 0.
    else:
        count += 1
        maxx = max(maxx, count)

print(maxx) # 731

f.close()
'''

# Task 2
'''
f = open('2.txt')

a = f.readline()
l = 0 # лок. макс.
maxx = 0 # глоб. макс.
s = '0123456789ABCDEF'

for i in a:
    if i in s: # Прямой метод
        l += 1
    else:
        maxx = max(maxx, l)
        l = 0

maxx = max(maxx, l)
print(maxx) # 16

f.close()
'''

# Task 3
'''
f = open('3.txt')

a = f.readline()

index = [] # Сохранение индексов всех J

for i in range(len(a)):
    if a[i] == "J":
        index.append(i)

maxx = 0
for i in range(len(index) - 5):
    # Просмотр 2х границ
    # И определение кол. эл., что стоят между ними
    maxx = max(maxx, index[i +  5] - index[i] - 1) 

file_count = f.read()
print(max(maxx, index[4], len(file_count) - index[-5] - 1)) # 105

f.close()


# От 5ой с конца буквы J до ...
'''

# Task 4
'''
f = open("4.txt").readline()
index = []
for i in range(len(f)):
    if f[i] == "M":
        index.append(i)

maxx = 0
for i in range(len(index) - 201):
    maxx = max(maxx, index[i + 201] - index[i] - 1)
print(max(maxx, index[200], len(f) - index[-201] - 1)) # 6508
'''

