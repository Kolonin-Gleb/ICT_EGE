# 9736
'''
На вход алгоритма подаётся натуральное число N.
Алгоритм строит по нему новое число R следующим образом.
1. Строится двоичная запись числа N.
2. Далее эта запись обрабатывается по следующему правилу:

а) если число N делится на 3, то в этой записи дописываются справа три последние двоичные цифры;
б) если число N на 3 не делится, то остаток от деления умножается на 3,

переводится в двоичную запись и дописывается в конец числа.
Полученная таким образом запись является двоичной записью искомого числа R.

3. Результат переводится в десятичную систему и выводится на экран.
Например, для исходного числа 12 = 11002 результатом является число 11001002 = 100,
а для исходного числа 4 = 1002 результатом является число 100112 = 19.

Укажите максимальное число R, не превышающее 170, которое может быть получено с помощью описанного алгоритма.
В ответе запишите это число в десятичной системе счисления.
'''

"""
lst = []
for N in range(4, 100): # начинаем с 4
    N_2 = bin(N)[2:]

    if N % 3 == 0:
        R = N_2 + N_2[-3:]
    else:
        R = N_2 + bin( (N % 3) * 3)[2:]

    # ПРОВЕРКА АЛГОРИТМА
    # if N < 13:
        # print(N, R)

    if int(R, 2) < 170:
        lst.append(int(R, 2))
print(max(lst)) # 166
"""

