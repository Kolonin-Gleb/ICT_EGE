# Типовое задание 6 Видеоурок

# Task 1 from video
# Повтори 5 [Вперёд 8 Направо 90]
# Определите, сколько точек с целочисленными координатами будут находиться внутри области,
# ограниченной линией, заданной данным алгоритмом. Точки на линии не учитывать
'''

from turtle import *
tracer(0) # отключение анимаций, для ускорения построений
# screensize(1000, 1000) # Установка размера окна
k = 50 # для установки масштаба

# Перемещение черепахи (код из задания)
left(90) # Задать начальное положение головы черепахи по Оу
for i in range(5):
    forward(8*k)
    right(90)

# Рисуем сетку координат
# Не только в положительной части координат, но и отрицательной
up()
for x in range(-20, 20):
    for y in range(-20, 20):
        # Перемещение черепахи в точку с заданными координатами
        setpos(x * k, y * k)
        # Установка точки
        dot(5, 'blue')

done() # чтобы окно не закрывалось автоматически
# Внутри квадрата 7 на 7 точек.
# Поэтому внутри квадрата 49
'''


# Task 2 from video #22:49
'''
from turtle import *
screensize(1000, 4000)
tracer(0)
k = 50

left(90) # Задать начальное направление головы черепахи по оУ
right(90) # Дальше начинается сам алгоритм из задания
for i in range(11):
    forward(10*k)
    right(90)

# Строим сетку координат
penup()
for x in range(-30, 30):
    for y in range(-30, 30):
        setpos(x * k, y * k)
        dot(5, 'blue')

# Answer 9*9=81
done()
'''

# Task 3 # Треугольник
'''
from turtle import *
# Первичная настройка
# screensize(1000, 1000)
tracer(0)
k = 40
left(90)

# Перемещение черепахи (Рисуем Границы)
for i in range(7):
    forward(10*k)
    right(120)

# Построение сетки координат (Точки)
penup()
for x in range(-30, 30):
    for y in range(-30, 30):
        setpos(x*k, y*k)
        dot(5, 'blue')

# Answer = 13+25 = 38
done()
'''

# Task 4 29:10
'''
from turtle import *
# Настройка черепахи
screensize(1000, 3000)
tracer(0)
k = 50
left(90)

# Перемещение черепахи (Границы)
for i in range(9):
    forward(12*k)
    right(120)

# Рисуем сетку (Точки)
penup()
for x in range(-30, 30):
    for y in range(-30, 30):
        setpos(x*k, y*k)
        dot(5, 'Blue')

# 31 + 25 = 56
done()
'''

# Task 5
'''
from turtle import *
# screensize(1000, 1000)
tracer(0)
k = 50
left(90)

right(45)
for i in range(7):
    forward(5*k)
    right(45)
    forward(10*k)
    right(135)

penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x*k, y*k)
        dot(5, 'blue')

# 6 + 21 = 27
done()
'''
