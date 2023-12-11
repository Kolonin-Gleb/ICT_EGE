# Ww Цц

# Task 1
'''
from turtle import *
speed(400)

k = 30
left(90) # Задать начальное положение головы черепахи по Оу

# Рисуем фигуру
for i in range(12):
    forward(4 * k)
    right(90)
    
# Рисуем систему координат
pu()

for col in range(6):
    for row in range(6):
        goto(col * k, row * k) # Перемещение в заданные координаты # Нужно домножить на то же значение, что использовалось выше.
        dot()

done()
'''

# Task 2
'''
from turtle import *
speed(400)
k = 50
left(90)

# Рисуем фигуру
for i in range(7):
    forward(6 * k)
    right(270)
    forward(8 * k)
    right(270)

pu()

# Система координат
for col in range(8):
    for row in range(8):
        goto(-col * k, row * k) # Добавил -, чтобы идти налево
        dot()

done()
'''

# Task 3
'''
from turtle import *
speed(400)
k = 50
left(90)

# Фигура
for i in range(6):
    forward(3 * k)
    right(90)
    forward(9 * k)
    right(90)

pu()

# Координаты
for col in range(10):
    for row in range(8):
        goto(col * k, row * k)
        dot()

done()
'''

# Task 4
'''
from turtle import *
speed(400)
k = 50
left(90)

# Фигура
right(270)
for i in range(11):
    forward(4 * k)
    right(90)
    forward(7 * k)
    right(90)

pu()

# Координаты
for col in range(10):
    for row in range(8):
        goto(-col * k, row * k)
        dot()

done()
'''

# Task 5
'''
from turtle import *

speed(400)
k = 20
left(90)

x = 12 # При каком значении точек будет 169 (включая те, что на линии)

# Фигура
for i in range(10):
    forward(x * k)
    right(90)

pu()
goto(0, 0)

# Координаты
for col in range(13):
    for row in range(13):
        goto(col * k, row * k)
        dot()

done()
'''

# Task 7
'''
from turtle import *

speed(400)
k = 20
left(90)

# Фигура
for i in range(7):
    forward(8 * k)
    right(120)

pu()
goto(0, 0)

# Координаты
for col in range(11):
    for row in range(11):
        goto(col * k, row * k)
        dot()

done()
'''

# Task 8
'''
from turtle import *

speed(400)
k = 20
left(90)


# Фигура
right(90)
for i in range(9):
    forward(10 * k)
    right(240)

pu()
goto(0, 0)

# Координаты
for col in range(11):
    for row in range(11):
        goto(col * k, row * k)
        dot()

done()
'''

# Task 9
'''
from turtle import *

speed(400)
k = 40

# Фигура
right(315)
for i in range(7):
    forward(12 * k)
    right(45)
    forward(6 * k)
    right(135)

pu()
goto(0, 0)

# Координаты
for col in range(16):
    for row in range(11):
        goto(col * k, row * k)
        dot()

done()
'''

# Task 10
'''
from turtle import *
speed(400)
k = 40

# Фигура
right(45)
stamp()
for i in range(18):
    forward(8 * k)
    right(135)
    forward(9 * k)
    right(45)

pu()

forward(8 * k) # Чтобы оказаться в правой нижней точке параллелограмма
setheading(90) # Смотреть в ось Y

# Координатная сетка
# Чтобы координатная сетка точно покрыла фигруру добавть в
# range -value +value

for col in range(-10, 25):
    for row in range(-5, 25):
        goto(col * k, row * k)
        dot()

done()
'''

# Task 11
'''
from turtle import *
speed(400)
k = 40
left(90)

for i in range(2):
    forward(7 * k)
    right(90)
    forward(11 * k)
    right(90)

pu()

back(-1 * k)
right(90)
forward(9 * k)
left(90)
pd()

for i in range(2):
    forward(8 * k)
    right(90)
    forward(3 * k)
    right(90)

# Коорданитная сетка
# Создаем ряд меток с высокой скоростью
pu()
speed(50000)
for x in range(25):
    for y in range(20):
        goto(x*k -90, y*k -170) # Перемещаем черепаху к указанным координатам
        dot()  # Оставляем отпечаток черепаши на холсте

done()
'''

# Task 12
'''
from turtle import *
speed(400)
k = 40
left(90)

for i in range(2):
    forward(10 * k)
    right(90)
    forward(18 * k)
    right(90)

pu()

back(-6 * k)
right(90)
forward(9 * k)
left(90)
pd()

for i in range(2):
    forward(17 * k)
    right(90)
    forward(5 * k)
    right(90)

# Коорданитная сетка
# Создаем ряд меток с высокой скоростью
pu()
speed(50000)
for x in range(25):
    for y in range(20):
        goto(x*k -90, y*k -170) # Перемещаем черепаху к указанным координатам
        dot()  # Оставляем отпечаток черепаши на холсте

done()
'''

# Task 13
'''
'''
