# Task 4
# for a in range(1, 1000):
#     f = True
#     for x in range(1, 500):
#         for y in range(1, 500):
#             if ((x > y) or (3 *x + 4*y < a) or (y > 15)) == 0:
#                 f = False
#                 break
#     if f == True:
#         print(a)
#         break

# Task 5

# POU / Monopoly / My game
''''''''''''''''''''''''''''''

# Моя команда: Глеб, Ксюша, Кирилл

# def F(s):
#     sm = 0
#     for x in s:
#         sm = sm + int(x)
#     return sm

# for n in range(4, 300):
    
#     s = '3' + n*'5' # 

#     while '25' in s or '333' in s or '555' in s:
#         if '25' in s:
#             s = s.replace('25', '3', 1)
#         if '355' in s:
#             s = s.replace('355', '52', 1)
#         if '555' in s:
#             s = s.replace('555', '23', 1)

#     if F(s) == 18:
#         print(n)

'''
for A in range(1, 10_000): # A - целое неотр. число
    if A % 100 == 0:
        print(f"progress = {A}")

    flag = True
    for x in range(1, 500):
        if ((x % A != 0) <= ((x % 6 == 0) <= (x % 21 != 0))) == 0: # Следует либо упростить формулу, либо расставить ()
            flag = False # Параметр не подошёл
            break
    if flag == True:
        print(A)
        # break # Т.к. просят найти наименьшее
'''
# 42

# def generate_numbers():
#     start_digit = 5
#     possibilities = [str(start_digit) + str(num) for num in range(0, 8)]
    
#     # Generating all possible combinations for the remaining 3 digits
#     for _ in range(3):
#         possibilities = [prefix + str(num) for prefix in possibilities for num in range(0, 8)]
    
#     return possibilities

# result = generate_numbers()
# print(len(result))

# Исходные параметры
width = 700
height = 960
compressed_size_kb = 360
compression_ratio = 0.45

# Рассчитываем исходный объем
original_size_kb = compressed_size_kb / (1 - compression_ratio)

# Рассчитываем бит на пиксель
bits_per_pixel = (original_size_kb * 8) / (width * height)

# Рассчитываем количество цветов
num_colors = 2 ** bits_per_pixel

print(f"Максимальное количество цветов: {int(num_colors)}")
