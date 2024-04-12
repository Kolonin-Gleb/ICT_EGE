# Task 1-3
'''
1 Куча
Ходы:
+1
*2
Win
S >=101
'''
"""
# s - тек. кол. камней
# m - ходы
# a = 1 ≤ S ≤ 100 -- для понимания в каком промежутке перебирать!
def f(s, m):
    if s >= 101:
        return m%2 == 0
    if m == 0:
        return 0
    # Рассматриваем все возможные ходы
    h = [f(s+1, m-1), f(s*2, m-1)]
    # Заученный стейтмент
    return any(h) if (m-1)%2 == 0 else all(h)


print("19)", [s for s in range(1, 101) if f(s, 2)]) # 50
print("20)", [s for s in range(1, 101) if not f(s, 1) and f(s, 3)]) # 25 49
print("21)", [s for s in range(1, 101) if not f(s,2) and f(s, 4)]) #  
"""

# Task 4-6
'''
1 Куча
Ходы:
+1
+2
*5
Win S >= 157
'''
"""
def f(s, m):
    if s >= 157:
        return m%2 == 0
    if m == 0:
        return 0
    
    h = [f(s+1, m-1), f(s+2, m-1), f(s*5, m-1)]
    return any(h) if (m-1)%2 == 0 else all(h) # all <-> any

# Известно, что Ваня выиграл своим первым ходом после неудачного 1ого хода Пети.
# Укажите минимальное значение S, когда такая ситуация возможна.

print("19)", [s for s in range(1, 157) if f(s, 2)]) # 7
print("20)", [s for s in range(1, 157) if not f(s, 1) and f(s, 3)]) # 29 30
print("21)", [s for s in range(1, 157) if not f(s, 2) and f(s, 4)]) # 28
"""



# 
'''
2 Кучи
Ходы:
+1
*2
S = a+b >= 257
a = 9
b = 1 ≤ S ≤ 247
'''
"""
def f(a, b, m):
    if a+b >= 257:
        return m%2 == 0
    if m == 0:
        return 0
    # Возможные ходы. Их воздействие на переменные
    h = [f(a+1, b, m-1), f(a, b+1, m-1), f(a*2, b, m-1), f(a, b*2, m-1)]

    return any(h) if (m-1)%2 == 0 else all(h) # all <-> any

# Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети.
# Укажите минимальное значение S, когда такая ситуация возможна.
print("19)", [b for b in range(1, 248) if f(9, b, 2)]) # 62
print("20)", [b for b in range(1, 248) if not f(9, b, 1) and f(9, b, 3)]) # 119 123
print("21)", [b for b in range(1, 248) if not f(9, b, 2) and f(9, b, 4)]) # 118
"""
