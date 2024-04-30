# 5952
'''
for x in '0123456789ABCDEF':
    num = int(f"10{x}A", 16) + int(f"FF{x}78", 16)
    if num % 19 == 0:
        print(num // 19) # 55238
        break
'''

# 7593
'''
for x in '0123456789ABCDE':
    num = int(f"97968{x}13", 15) + int(f"7{x}213", 15)
    if num % 14 == 0:
        print(num // 14) # 116070624
        break
'''

# 6086
'''
for x in '0123456789ABCDEFGH':
    num = int(f"451{x}", 18) + int(f"79{x}2", 18)
    if num % 27 == 0:
        print(num // 27)#2556
        break
'''


# 6267
'''
num1 = 0
for x in '0123456789abcdefghijklmnopqrstuvwxyz':
    res = int(f"12{x}45", 36) + 1*12345 + int(x, 36)
    if res % 13 == 0:
        print(x, res//13) # Нужно наибольшее => последний вывод
# 140433 - ответ
'''

# 6788
# Особенность данной задачи - очень большая С.С. (68)
'''
# Перебор x от больших к меньшим
for x in range(67, -1, -1): # Возможные знач. х в 68 С.С. - от 0 до 67 вкл.
    num1 = 5 + x * 68 + 3 * 68**2 + 2 * 68**3 + 68**4
    num2 = 3 + 3*68   + 2 * 68**2 + x * 68**3 + 68**4
    if (num1 + num2) % 12 == 0:
        print( (num1 + num2) // 12) # 5321454
        break
'''
