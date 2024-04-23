
'''
f = open('26_7602.txt')
# f = open('26_test.txt')


k = int(f.readline()) # кол. во ячеек
n = int(f.readline()) # кол. багажей/пассажиров

a = []

for i in range(n):
    # Проход по парам
    start, end = map(int, f.readline().split())
    a.append([start, end])

# Построили очередь
a.sort()
# print(a)
# Обработка очереди пассажирова

camera=[0]*k # кол. во ячеек
count = 0    # кол. успешно принятого багажа
last = 0     # куда положили последний багаж

for i in range(n):
    start, end = a[i]
    for j in range(k): # проход по ячейкам
        if camera[j] < start:
            camera[j] = end
            count += 1
            last = j+1 # нумерация ячеек начинаетя с 1.
            break

print(count, last) # 586 3

f.close()
'''

# Задачка Maximum
'''
'''
f = open('5_maximum.txt')
# f = open('5_maximum_test.txt')

k = int(f.readline()) # кол. машин доставки
n = int(f.readline()) # кол. партий товара

a = []

for i in range(n):
    # Проход по парам
    start, end = map(int, f.readline().split())
    a.append([start, end])

# Построили очередь доставки партий товара
a.sort()
# print(a[-1][0] // 60) # Отправка товара улолжится в сутки

# Обработка очереди отправки товара

car=[0]*k # кол. во машин доставки
count = 0    # кол. использованных Экспресс доставок
last = 0     # последняя вернувшаяся машина

for i in range(n):
    start, end = a[i]
    for j in range(k): # проход по машина
        if car[j] < start: # Разница между возращением машины и принятием нового товара должна быть 1 (строгое неравенство)
            car[j] = end
            # if car[j] >= max(car):
            #     last = j+1 # нумерация машин начинаетя с 1. # Машина, что вернётся последней
            break
    # Если в цикле не сработал break
    else: # сработает else цикла for!!!! В Python есть такая фишка.
        count += 1


# print(count, last) # 822 31
print(count, car.index(max(car)) + 1) # 822 31


f.close()
