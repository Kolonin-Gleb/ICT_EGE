# kompege 9840
'''
В файле содержится последовательность целых чисел.
Элементы последовательности могут принимать целые значения от -100 000 до 100 000 включительно.

Определите количество пар последовательности, в которых только

один из элементов является четырёхзначным числом,
а КВАДРТА СУММЫ элементов пары не больше КВАДРАТА!!! максимального элемента последовательности,
являющегося четырёхзначным числом и оканчивающегося на 39.
В ответе запишите количество найденных пар чисел,
затем максимальную из сумм элементов таких пар.
 
В данной задаче под парой подразумевается два идущих подряд элемента последовательности.
'''

# f = open('17_9840.txt')

# s = [int(x) for x in f]

# mmax = -9999999999999999999

# for el in s:
#     if len(str(el)) == 4 and abs(el) % 100 == 39:
#         mmax = max(mmax, el)

# print("mmax = ", mmax)

# sum_max = -9999999999999999999

# count = 0
# for i in range(len(s) - 1): # На будущее используй сравнения с числами <= <
#     if ((len(str(abs(s[i]))) == 4 and len(str(abs(s[i+1]))) != 4) or (len(str(abs(s[i]))) != 4 and len(str(abs(s[i+1]))) == 4)) \
#         and (s[i] + s[i+1])**2 <= mmax**2:

#         sum_max = max(sum_max, s[i] + s[i+1])
#         count += 1


# print(count, sum_max) # 1799 9231
# # mmax = len(abs(max(lst))) == 4 % 100 == 39
# # >999
# # (a+b)**2 <= 

# f.close()


# № 9839 Основная волна 27.06.23 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(100_000)

def F(n):
    if n < 7:
        return 7
    return n + 1 + F(n-2)

print(F(2024) - F(2020))
'''


# Оптимизация!
'''
f = [7] * 10_000

for n in range(7, 10_000):
    f[n] = n + 1 + f[n-2]

print(f[2024] - f[2020])
'''

# Task 9844 
'''
Исполнитель преобразует число на экране. У исполнителя есть три команды, которые обозначены латинскими буквами:

А. Вычесть 1
В. Вычесть 3
С. Найти целую часть от деления на 2

Программа для исполнителя — это последовательность команд.
Сколько существует программ, для которых при исходном числе 19 результатом является число 3,
 при этом траектория вычислений не содержит числа 7 и содержит 10?

Траектория вычислений программы — это последовательность результатов выполнения всех команд программы.
Например, для программы СВА при исходном числе 13 траектория будет состоять из чисел 6, 3, 2.
'''
"""
def F(s, e):
    if s == e:
        return 1
    if s < e or s == 7:
        return 0

    return F(s-1, e) + F(s-3, e) + F(s//2, e)


print(F(19, 10) * F(10, 3))
"""


# 9752
'''
Исполнитель преобразует число на экране.
У исполнителя есть три команды, которым присвоены номера:
A. Прибавить 2
B. Прибавить 3
C. Умножить на 2
Программа для исполнителя – это последовательность команд.

Сколько существует программ, для которых при исходном числе 3 результатом является число 25,
и при этом траектория вычислений содержит число 10 и не содержит 17?

Траектория вычислений программы – это последовательность результатов выполнения всех команд программы.
Например, для программы CBA при исходном числе 7 траектория состоит из чисел 14, 17, 19.
'''


def F(s, e):
    if s > e or s == 17:
        return 0
    elif s == e:
        return 1
    return F(s+2, e) + F(s+3, e) + F(s*2, e)


print(F(3, 10)*F(10, 25))