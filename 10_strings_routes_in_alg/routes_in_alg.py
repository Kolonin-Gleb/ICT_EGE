# Task 1
'''
def F(x, y):
    if x > y: # Уже перескочили. Назад никак
        return 0
    elif x == y:
        return 1
    else:
        return F(x + 1, y) + F(x + 2, y)

print(F(1, 15))
'''

# Task 2
'''
def F(x, y):
    if x < y: # Уже перескочили. Вперед никак
        return 0
    elif x == y:
        return 1
    else:
        return F(x - 2, y) + F(x - 3, y)

print(F(21, 1))
'''

# Task 3
'''
def F(x, y):
    if x < y:
        return 0
    elif x == y:
        return 1
    else:
        return F(x - 2, y) + F(x - 6, y)

print(F(35, 7))
'''

# Task 4
'''
def F(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    else:
        return F(x + 1, y) + F(x + (x+1), y)

print(F(3, 28))
'''

# Task 5
'''
def F(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    else:
        return F(x+1, y) + F(x*4, y)

print(F(1, 76))
'''

# Task 6
'''
def F(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    else:
        return F(x+1, y) + F(x+2, y) + F(x + (x-1), y)

print(F(2, 16))
'''

# Task 7
# 1) +1
# 2) Чётное число *1.5
'''
def F(x, y):
    if x > y or x == 31:
        return 0
    elif x == y:
        return 1
    else:
        if x % 2 == 0:
            return F(x+1, y) + F(1.5*x, y)
        else:
            return F(x+1, y)

print(F(2, 56))
'''

# Task 8
'''
def F(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    else:
        return F(x+1, y) + F(x*2, y) + F(2*x + 1, y) + F(x*10, y)

print(F(7, 78))
'''

# Task 9
'''
def F(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    else:
        return F(x+2, y) + F(x*2, y)

print(F(4, 14) * F(14, 68))
'''

# Task 10
'''
def F(x, y):
    if x > y or x == 56:
        return 0
    elif x == y:
        return 1
    else:
        return F(x + 1, y) + F(2*x+1, y)

print(F(1, 67))
'''

# Task 11
'''
def F(x, y):
    if x > y or x == 19:
        return 0
    elif x == y:
        return 1
    else:
        return F(x + 1, y) + F(x + 2, y) + F(2*x+1, y)

print(F(5, 15) * F(15, 21))
'''

# Task 12
'''
def F(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    else:
        return F(x+1, y) + F(x+2, y) + F(x*2, y)

print(F(2, 8) * F(8, 12) * F(12, 16))
'''

# Task 13
'''
def F(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    else:
        if str(x)[0] == 9:
            return F(x + 1, y)
        else:
            x_upgraded = str(int(str(x)[0]) + 1) + str(x)[1:]
            return F(int(x_upgraded), y) + F(x + 1, y)

print(F(10, 43))
'''
