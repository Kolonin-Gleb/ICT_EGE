# 12234
'''
print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if (y and (x or z) or not (y or z) or w) == 0:
                    print(x, y, z, w)
# xywz
'''

# 10084
'''
print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ( (x and not y) or (y == z) or not w ) == 0:
                    print(x, y, z, w)

# wzyx
'''

# 9825
# Похоже, что тут нужно учесть приоритет операций!
'''
print('x y z w')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ( (x <= (z == w)) or not (y <= w) ) == 0:
                    print(x, y, z, w)
'''
# zwyx

# 9771
'''
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ( (y <= x) and not(z) and w ) == 1:
                    print(x, y, z, w)
# wxyz
'''

# TODO: 485
# При решении этой авторской задачи, нужно верно расставить приоритет операций с помощью ()
# if ( (a == b) or (c == b) ) == 1: --- НЕВЕРНО
# if ( a == (b or c) == b ) == 1: --- ВЕРНО

"""
print("a b c")
for a in 0,1:
    for b in 0,1:
        for c in 0,1:
            if ( a == (b or c) == b ) == 1:
                print(a, b, c)

# Вывод не подходит для таблицы, что предстоит заполнить. 
# Почему?
# a b c
# 0 0 0
# 1 1 0
# 1 1 1
"""

# 7023
'''
'''
