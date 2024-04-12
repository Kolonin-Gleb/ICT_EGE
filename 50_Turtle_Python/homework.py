# Task 1
'''
from turtle import *
# screensize(1000, 1000)
tracer(0)
k = 50
left(90)


for i in range(12):
    forward(4*k)
    right(90)

penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x*k, y*k)
        dot(5, 'blue')

done()
'''

# Task 2
'''
from turtle import *
# screensize(1000, 1000)
tracer(0)
k = 50
left(90)

right(90)
for i in range(7):
    forward(6*k)
    right(270)
    forward(8*k)
    right(270)

penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x*k, y*k)
        dot(5, 'blue')

done()
'''

# Task 3, 4, 
'''
from turtle import *
screensize(1000, 4000)
tracer(0)
k = 50
left(90)

x = 12 # Подбор значения

for i in range(10):
    forward(x*k)
    right(90)

penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x*k, y*k)
        dot(5, 'blue')

# ВАЖНО! ВКЛЮЧАЯ точки на линиях
print(169**0.5)
# Поэтому ответ 12
done()
'''

# Task 6
'''
from turtle import *
# screensize(1000, 1000)
tracer(0)
k = 50
left(90)

right(90)
for i in range(9):
    forward(10*k)
    right(240)

penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x*k, y*k)
        dot(5, 'blue')

done()
'''

# Task 7
'''
from turtle import *
screensize(1000, 3000)
tracer(0)
k = 50
left(90)

right(315)
for i in range(7):
    forward(12*k)
    right(45)
    forward(6*k)
    right(135)

penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x*k, y*k)
        dot(5, 'blue')

done()
'''

# Task 10
'''
from turtle import *
# screensize(1000, 1000)
tracer(0)
k = 50
left(90)

right(45)
for i in range(18):
    forward(8*k)
    right(135)
    forward(9*k)
    right(45)

penup()

for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x*k, y*k)
        dot(5, 'blue')
done()
'''

# Task 41
'''
from turtle import *
# screensize(1000, 1000)
tracer(0)
k = 50
left(90)

for i in range(2):
    forward(7*k)
    right(90)
    forward(11*k)
    right(90)

penup()
back(-1*k) # это ведь равносильно вперёд?)
right(90)
forward(9*k)
left(90)
pendown()

for i in range(2):
    forward(8*k)
    right(90)
    forward(3*k)
    right(90)

penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x*k, y*k)
        dot(5, 'blue')

done()
'''

# Task 12
'''
'''
from turtle import *
screensize(2000, 4000)
tracer(0)
k = 40
left(90)


for i in range(2):
    forward(7*k)
    right(90)
    forward(18*k)
    right(90)

penup()
back(6*k)
right(90)
forward(9*k)
left(90)
pendown()

for i in range(2):
    forward(13*k)
    right(90)
    forward(9*k)
    right(90)

penup()
for x in range(-20, 20):
    for y in range(-20, 20):
        setpos(x*k, y*k)
        dot(5, 'green')

# включая точки на линиях.
done()


