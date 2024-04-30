# № 4704 Демоверсия 2023 (Уровень: Базовый)
'''
import sys
sys.setrecursionlimit(9999)

def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n - 1)


print(F(2023) // F(2020)) # 8266912626
'''

# 4676
'''
def f(n):
    if n < 3:
        return 1
    if n > 2 and n % 2 == 0:
        return 2 * f(n - 1) - f(n - 2)
    if n > 2 and n % 2 != 0:
        return f(n - 1) - 2 * f(n - 2) - 3

print(f(15)) # 6
'''
# 9945
# В подобное задаче нужно переписать функцию, чтобы она могла выполниться успешно и дать верный ответ.
'''
def F(n):
    k = 2
    if n > 1:
        k += F(n-2) + F(n // 2) + 1
    return k

print(F(127)) # 127547
'''

# 600
'''
def F(n):
    k = 1
    if n>=1:
        k += 1
        k += F(n-1) + F(n-2)
    return k

print(F(28)) # 2496118
'''

