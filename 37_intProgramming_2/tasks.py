# Задание 25 в ЕГЭ
'''
n = int(input()) # Принимаем число
k = 0 # кол. делителей

for i in range(1, n):
    if n % i == 0:
        k = k + 1

n = int(input())
k = 0
for i in range(1, n):
    if n % i == 0:
        k = k + 1

print(k)
'''

# Task 1
# Найти числа имеющие ровно два различных натуральных делителя
# в порядке убывания произведения этих двух делителей. ДЛЯ КАЖДОГО ЧИСЛА!!!
# Делители в строке должны следовать в порядке возрастания.
'''
x = 153_381
y = 153_419

for i in range(y, x - 1, -1): # Идём в обратном порядке, т.к. в порядке убывания произведения этих двух делителей
    a = [] # для сохранения делителей
    for j in range(2, i // 2 + 1): # Нет смысла искать делители в числах, что больше половины i
        if i % j == 0:
            a.append(j)

    if len(a) == 2: # Если ровно 2 делителя
        print(a[0], a[1]) # Делители в порядке возрастания.
'''

# Task 2
'''
# числа, имеющие ровно 4 РАЗЛИЧНЫХ НЕЧЁТНЫХ натуральных делителей
# в порядке убывания произведения этих четырёх делителей.
# Делители в строке должны следовать в порядке убывания.

x = 17_144
y = 17_238
# x = 17
# y = 65

for i in range(y, x - 1, -1):
    a = []
    for j in range(2, i // 2 + 1):
        if i % j == 0 and j % 2 != 0:
            a.append(j)
    
    if len(a) == 4:
        print(a[::-1])
'''

# Task 3
# ровно один нечётный натуральный делитель
# делитель и последнюю цифру найденного числа
# в порядке ВОЗРАСТАНИЯ этих делителей.
'''
x = 104_542
y = 104_611

for i in range(x, y + 1, 1):
    a = []
    for j in range(3, i // 2 + 1, 2): # От 3 до половины числа с шагом 2
        if i % j == 0:
            a.append(j)
    if len(a) == 1:
        print(a[0], i % 10)
'''

# Task 4
# Поиск простых чисел
# Сумма 2х последних цифр 
# В порядке возрастания найденных чисел
'''
def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

x = 95_322
y = 95_504

for i in range(x, y + 1):
    if is_prime(i):
        print(i, (i % 100) // 10 + i % 10)
'''

# Task 5
# Простое число
# Порядковый среди найденных
# Предпоследняя цифра числа
# В порядке возрастания
'''
x = 762_423
y = 762_579

def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

k = 0
for i in range(x, y + 1):
    if is_prime(i):
        k += 1
        print(k, i % 100 // 10)
'''

# Task 6
# большие 166_789
# значение M при делении на 7 дает в остатке 3
# Вывести первые 6 из значения M
'''
M = 0 # мин дел + макс дел
k = 0
i = 166_789

while k != 6:
    i += 1
    a = []
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            a.append(j)
    
    if len(a) != 0:
        M = min(a) + max(a)
    
    if M % 7 == 3:
        print(i, M)
        k += 1
'''
# Correct solution
'''
i = 166790
count = 0
while count != 6:
    a = []
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            a.append(j)
    if len(a) > 1:
        M = a[0] + a[-1]

        if M % 7 == 3:
            count += 1
            print(i, M)
    i += 1
'''

# Task 7
# Больше 433_546
# M - Абсолютная разность мин и макс делителей. иначе = 0
# M % 10 = 5
# первые 9 найденных чисел и соответствующие им значения M.⠀
'''
i = 433_546
count = 0
while count != 9:
    a = []
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            a.append(j)
    if len(a) > 1:
        M = abs(a[0] - a[-1])
        if M % 10 == 5:
            print(i, M)
            count += 1
    i += 1
'''

# Task 8
# большие 345_844
# M — абсолютная разность минимального и максимального четных натуральных делителей
# M оканчивается на 4.
# Вывести первые 8 найденных чисел и соответствующие им значения M.
'''
i = 345_844 # 
count = 0   # 
while count != 8: 
    a = []
    for j in range(2, i // 2 + 1, 2): 
        if i % j == 0: 
            a.append(j)
    if len(a) > 1: 
        M = abs(a[0] - a[-1])
        if M % 10 == 4: 
            print(i, M)
            count += 1
    i += 1
'''

# Task 9
# S — это отличная от нуля сумма цифр числа
# меньших 677853
# 6 самых больших простых чисел, у которых S кратно 4
# число и соответствующее S
'''
def is_prime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True
def sum_digit(n):
    s = 0
    while n > 0:
        s += n % 10
        n = n // 10
    return s

i = 677_853
count = 0

while count != 6:
    if is_prime(i):
        s = sum_digit(i)
        if s % 4 == 0:
            print(i, s)
            count += 1
    i -= 1
'''

# Task 10
'''

def is_any_even(n):
    if any(char in '02468' for char in str(n)):
        return True
    else:
        return False

def mul_even_digits(n):
    if is_any_even(n):
        m = 1
        while n > 0:
            tmp = n % 10
            if tmp % 10 == 2:
                m *= tmp
            n = n // 10
        return m
    return 0

# Пусть M — это произведение четных цифр числа.
# Если в числе нет четных цифр, то считаем M равным нулю.
# Напишите программу, которая найдет среди целых чисел, больших 355_438
# 5 первых простых чисел, у которых M не кратно 8.

i = 200 # больших
k = 0

while k != 5:
    M = mul_even_digits(i)
    if M % 8 != 0:
        k += 1
        print(i, M)

    i -= 1
'''


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def product_of_even_digits(num):
    product = 1
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            product *= digit
        num //= 10
    return product

def find_primes_with_odd_product(starting_number, count):
    found = 0
    number = starting_number + 1
    while found < count:
        if is_prime(number):
            product = product_of_even_digits(number)
            if product % 8 != 0:
                print(number, product)
                found += 1
        number += 1

starting_number = 355438
count = 5
find_primes_with_odd_product(starting_number, count)
