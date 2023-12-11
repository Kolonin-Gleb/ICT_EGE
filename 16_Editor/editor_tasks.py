# w

# Task 1
'''
s = '3' * 78

while '3333' in s or '7777' in s:
    # print(s) # fod debugging
    if '3333' in s:
        s = s.replace('3333', '77', 1)
    else:
        s = s.replace('7777', '33', 1)

print(s)
'''

# Task 2
'''
s = '5'*44 + '3'

while '322' in s or '553' in s:
    if '322' in s:
        s = s.replace('322', '53', 1)
    else:
        s = s.replace('553', '32', 1)

print(s)
'''

# Task 3
'''
s = '4'*9+'5'*12

while '444' in s or '888' in s:
    if '444' in s:
        s = s.replace('444', '8')
    while '555' in s:
        s = s.replace('555', '8')
    while '888' in s:
        s = s.replace('888', '3')

print(s)
'''

# Task 4
'''
import random

s = list('1'*12+'3'*39+'5'*7)
random.shuffle(s)
s = '>'+''.join(s)

while '>1' in s or '>3' in s or '>5' in s:
    if '>1' in s:
        s = s.replace('>1', '2>', 1)
    if '>3' in s:
        s = s.replace('>3', '012>', 1)
    if '>5' in s:
        s = s.replace('>5', '5>', 1)

summa = 0
for dig in s[:-1]:
    summa += int(dig)

print(summa)
'''

# Task 5
'''
s = '*'+'7'*58

while '*77' in s or '*' in s:
    if '*77' in s:
        s = s.replace('*77', '7*')
    else:
        if '*' in s:
            s = s.replace('*', '777')

print(s.count('7'))
'''

# Task 6
'''
import random

s = list('2'*33+'3'*15+'4'*6)
random.shuffle(s)
s = '1' + s

summa = 0

while '12' in s or '13' in s or '14' in s:
    if '12' in s:
        s = s.replace('12', '31')
    if '13' in s:
        s = s.replace('13', '441')
    if '14' in s:
        s = s.replace('14', '221')

s = s.replace('1', '333')

summa = 0
for dig in s:
    summa += int(dig)

print(summa)
'''

# Task 7

#  15 цифр 0, 20 цифр 1 и 25 цифр 2, расположенных в произвольном порядке.
# Запишите без разделителей символы, которые имеют порядковые номера 15, 20 и 50 в получившейся строке.
'''
import random

s = list('0'*15+'1'*20+'2'*25)
random.shuffle(s)

s = ''.join(s)

while '01' in s or '02' in s or '12' in s:
    if '01' in s:
        s = s.replace('01', '10')
    if '02' in s:
        s = s.replace('02', '20')
    if '12' in s:
        s = s.replace('12', '21')

print(s[14], s[19], s[49])
'''

# Task 8
# 30 цифр 5, 30 цифр 7 и 30 цифр 9, расположенных в произвольном порядке.
# Запишите без разделителей символы, которые имеют порядковые номера 15, 45 и 60 в получившейся строке.
'''
import random

s = list('5'*30+'7'*30+'9'*30)
random.shuffle(s)

s = ''.join(s)

while '59' in s or '75' in s or '79' in s:
    if '59' in s:
        s = s.replace('59', '95')
    if '75' in s:
        s = s.replace('75', '57')
    if '79' in s:
        s = s.replace('79', '97')

print(s[14], s[44], s[59])
'''

# Task 9
# На вход приведённой выше программе поступает строка, начинающаяся с символа «>»,
# а затем содержащая 23 цифры «0», 18 цифр «1» и n цифр «2», расположенных в произвольном порядке.
# Определите наименьшее значение n, при котором сумма числовых значений цифр строки,
# получившейся в результате выполнения программы, является простым числом.

'''
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

import random

n = -1 # Стартовое наименьшее число

while True:
    n += 1
    s = list('0'*23+'1'*18+'2'*n)
    random.shuffle(s)
    s = '>' + ''.join(s)

    while '>0' in s or '>1' in s or '>2' in s:
        if '>0' in s:
            s = s.replace('>0', '22>', 1)
        if '>1' in s:
            s = s.replace('>1', '2>', 1)
        if '>2' in s:
            s = s.replace('>2', '23>', 1)

    summa = 0
    for dig in s[:-1]:
        summa += int(dig)

    if is_prime(summa):
        print(n)
        break
'''

# Task 10
# Определите наименьшее значение n, при котором сумма числовых значений цифр строки, 
# получившейся в результате выполнения программы, является простым числом.
'''
import random

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

n = -1

while True:
    n += 1
    summa = 0

    s = list('5'*12+'6'*21+'7'*n)
    random.shuffle(s)
    s = '1' + ''.join(s)

    while '15' in s or '16' in s or '17' in s:
        if '15' in s:
            s = s.replace('15', '221')
        if '16' in s:
            s = s.replace('16', '41')
        if '17' in s:
            s = s.replace('17', '51')

    for dig in s:
        summa += int(dig)

    if is_prime(summa):
        print(n)
        break
'''

# Task 11
# 
'''
n = 3

while True:
    n += 1
    s = '5' + '2'*n
    summa = 0

    while '72' in s or '522' in s or '2222' in s:
        if '72' in s:
            s = s.replace('72', '2', 1)
        if '522' in s:
            s = s.replace('522', '27', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
    
    for dig in s:
        summa += int(dig)

    if summa == 66:
        print(n)
        break
'''

# Task 12
'''
n = 3

while True:
    n += 1
    s = '6' + '2'*n
    summa = 0

    while '63' in s or '322' in s:
        if '63' in s:
            s = s.replace('63', '2', 1)
        if '322' in s:
            s = s.replace('322', '26', 1)
    
    for dig in s:
        summa += int(dig)

    if summa == 200:
        print(n)
        break
'''

# Task 13
'''
n = 3

while True:
    n += 1
    s = '2' + '5'*n

    print(s)

    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '5', 1)
        if '355' in s:
            s = s.replace('355', '52', 1)
        if '555' in s:
            s = s.replace('555', '3', 1)
    
    if s.count('3') == 2:
        print(n)
        break
'''

# Task 14
# На вход приведённой выше программе поступает строка, начинающаяся с цифры «3», 
# а затем содержащая n цифр «5» (n > 3).
# Определите наименьшее значение n, при котором в строке,
# получившейся в результате выполнения программы, останутся только цифры «5».
'''
n = 3

while True:
    n += 1
    s = '3' + '5'*n

    while '25' in s or '355' in s or '555' in s:
        if '25' in s:
            s = s.replace('25', '5', 1)
        if '355' in s:
            s = s.replace('355', '52', 1)
        if '555' in s:
            s = s.replace('555', '3', 1)
    
    if s.count('5') == len(s):
        print(n)
        break
'''

# Task 15
# На вход приведённой выше программе поступает строка, начинающаяся с цифры «1»,
# а затем содержащая n цифр «9» (3 < n < 10 000).
# Определите наибольшее возможное значение суммы числовых значений цифр в строке,
# которая может быть результатом выполнения программы.
'''

sums = [] # Можно написать более оптимизированный код используя max_sum = max(max_sum, summa)

for n in range(3, 10000+1):
    # print(n)
    s = '1' + '9'*n

    while '19' in s or '49' in s or '999' in s:
        if '19' in s:
            s = s.replace('19', '9', 1)
        if '49' in s:
            s = s.replace('49', '91', 1)
        if '999' in s:
            s = s.replace('999', '4', 1)

    summa = 0
    for dig in s:
        summa += int(dig)

    sums.append(summa)

print(max(sums))
'''

# Task 16
'''
'''

