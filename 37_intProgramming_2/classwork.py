# Course book page 96
'''
'''

# Ex 1
# Среди чисел в дипозоне [x, y] найти у числа
# РОВНО 2 делителя (не считая 1 и самого числа)
# # Выводить два найденных делителя для таких чисел в порядке возрастания в 2 столбца (через пробел)
'''
x = 174457
y = 174502

for i in range(x, y + 1):
    a = []
    for j in range(2, i // 2 + 1): # Нет смысла искать делители в числах, что больше половины i
        if i % j == 0:
            a.append(j) # Сохраняем делители
    if len(a) == 2: # Если делителей РОВНО 2
        print(a[0],  a[1])
'''
    
# Ex 2
# РОВНО 1 натуральный ЧЁТНЫЙ делитель  (не считая 1 и самого числа)
# В порядке убывания РАССМАТРИВАЕМОГО ЧИСЛА (само число и его делитель)
'''
x = 714718
y = 714502

for i in range(y, x - 1, -1): # Идём в обратном порядке 
    a = []
    for j in range(2, i//2 + 1):
        if j % 2 == 0 and i % j == 0:
            a.append(j)
    if len(a) == 1:
        print(i, a[0])
'''

# Ex 3
# TODO: Миша покажет
'''
i = 45201
k = 0

while k != 5:
    a = [] # Массив делителей
    M = 0
    for j in range(2, i //2 + 1):
        if j % 2 == 0 and i % j == 0:
            a.append(j)
        if len(a) > 1:
            M = a[0] + a[-1]
            if M % 7 == 3:
                print(i, M)
                k += 1
    i += 1
'''

# Ex 5
'''
def sum_digit(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s

def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

i = 554886
k = 0 
while k != 5:
    S = sum_digit(i)

    if is_prime(S) % 5 == 0 and S % 5 == 0:
        print(i, S)
        k += 1
    i-= 1
'''
# Ex 6
'''
def mul_odd_digit(n):
    s = 1
    while n > 0:
        if (n % 10) % 2 != 0:
            s *= n % 10
        n = n // 10
    return s
def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

i = 615223
k = 0
while k != 6:
    M = mul_odd_digit(i)

    if is_prime(i) and M % 10 == 5:
        print(i, M)
        k += 1
    i+= 1
'''


