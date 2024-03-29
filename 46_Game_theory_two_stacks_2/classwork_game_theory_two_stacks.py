# Данный сайт позволяет визуализировать рекурсию, что полезно при работе с Теорией Игр.
# recursion.vercel.app

# Теория игр Тип 19

# numbers = [1, 2, 3, 4, 5]
# print(all(n > 0 for n in numbers))
# print(any(n > 0 for n in numbers))

'''
def f(s, m):
    if s >= 59: return m%2 == 0
    if m == 0: return 0
    h = [f(s + 2, m -1), f(s + 3, m -1), f(s * 2, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)

print("19)", min([s for s in range(1, 58) if f(s, 2)])) # 15 # Here all should be replaced with any
print("20)", [s for s in range(1, 58) if not f(s, 1) and f(s, 3)][:2]) # 14, 25
print("21)", max([s for s in range(1, 58) if not f(s, 2)  and f(s, 4)])) # 24
'''



# Code from lesson
'''
def f(a, b, m):
    if a + b >= 231: return m % 2 == 0
    if m == 0: return 0
    h = [f(a +1, b, m -1), f(a * 2, b, m -1), f(a, b + 1, m -1), f(a, b*2, m -1)]
    return any(h) if (m-1) % 2 == 0  else all(h)

print("19)", [s for s in range(1, 214) if f(17, s, 2)]) # 54 all => any
print("20)", [s for s in range(1, 214) if  not f(17, s, 1) and f(17, s, 3)]) # 98 106
print("21)", [s for s in range(1, 214) if not f(17, s, 2) and  f(17, s, 4)]) # 97 105
'''

'''
def f(s, m):
    if s >= 59: return m%2 == 0
    if m == 0: return 0
    h = [f(s + 2, m -1), f(s + 3, m -1), f(s * 2, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)

print("19)", [s for s in range(1, 58) if f(s, 2)]) # 15 all => any
print("20)", [s for s in range(1, 58) if not f(s, 1) and f(s, 3)]) # 14, 25
print("21)", [s for s in range(1, 58) if not f(s, 2)  and f(s, 4)]) # 2
'''

'''
def f(s, m):
    if s >= 59: return m%2 == 0
    if m == 0: return 0
    h = [f(s + 2, m -1), f(s + 3, m -1), f(s * 2, m - 1)]
    return any(h) if (m - 1) % 2 == 0 else all(h)

print("19)", [s for s in range(1, 58) if f(s, 2)]) # 15
print("20)", [s for s in range(1, 58) if not f(s, 1) and f(s, 3)]) # 14, 25
print("21)", [s for s in range(1, 58) if not f(s, 2)  and f(s, 4)]) # 24
'''
