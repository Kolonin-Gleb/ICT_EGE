# 7584
'''
На вход алгоритма подаётся натуральное число N.
Алгоритм строит по нему новое число R следующим образом.

1. Строится двоичная запись числа N.
2. Далее эта запись обрабатывается по следующему правилу:

а) если число кратно 3, тогда в конец дописывается три младших разряда полученной двоичной записи,

б) если число не кратно 3, тогда в конец дописывается двоичная последовательность,
являющаяся результатом умножения 3 на остаток от деления числа N на 3.

Полученная таким образом запись является двоичной записью искомого числа R.

# ПРОВЕРКА АЛГОРИТМА

Например, для исходного числа 5(10) = 101(2) результатом является число 101110(2) = 46(10),
а для исходного числа 9(10) = 1001(2) результатом является число 1001001(2) = 73(10).

Укажите наибольшее число N, после обработки которого с помощью этого алгоритма получается число R, меньшее 100.
В ответе запишите это число в десятичной системе счисления.
'''

# Берем с 4, так как числа меньше не дадут нам 3-ех цифр в двоичной системе
"""
lst = []
for N in range(4, 100):
    N_2 = bin(N)[2:]

    if N % 3 == 0:
        R = N_2 + N_2[-3:]
    else: # 3 на остаток от деления числа N на 3.
        R = N_2 + bin((N % 3) * 3)[2:]

    # ПРОВЕРКА АЛГОРИТМА
    # if N < 10:
    #     print(N, R)
    # else:
    #     break
    if int(R, 2) < 100:
        lst.append(N)

print(max(lst)) # 22
"""
