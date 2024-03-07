# Тип 12 Исполнитель редактор
'''
s = '9' * 84

while '33333' in s or '999' in s:
    if '33333' in s:
        s = s.replace('33333', '99', 1)
    else:
        s = s.replace('999', '3', 1)

print(s) # 33
'''

# 
'''
s = '1' + '8' * 80

while '18' in s or '288' in s or '3888' in s:
    if '18' in s:
        s = s.replace('18', '2', 1)
    else:
        if '288' in s:
            s = s.replace('288', '3', 1)
        else:
            s = s.replace('3888', '1', 1)

print(s) # 28
'''

# Task (-2)
'''
import random

def sum_digits(n):
    res = 0
    while n > 0:
        res += n % 10
        n = n // 10
    return res

s = '1' * 11 + '2' * 12 + '3' * 30
s = list(s)
random.shuffle(s)
s = '>' + ''.join(s)

while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s:
        s = s.replace('>1', '22>', 1)
    elif '>2' in s:
        s = s.replace('>2', '2>', 1)
    elif '>3' in s:
        s = s.replace('>3', '1>', 1)

print(sum_digits( int(int(s[:-1])) )) # 98
'''




