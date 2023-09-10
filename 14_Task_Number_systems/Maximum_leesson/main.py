# Task 16
'''
# 10101010(2) + 123214(5) + 13212AD(16) – 212321(4). 
# Ответ дайте в восьмеричной системе счисления

dig1 = int('10101010', 2)
dig2 = int('123214', 5)
dig3 = int('13212AD', 16)
dig4 = int('212321', 4)

print(oct(dig1 + dig2 + dig3 - dig4))
'''

# Task 16
'''
DA156(21) + FF3200(19) – AB2134(13) + D8CCF(17) 

print(hex(int('DA156', 21) + int('FF3200', 19) - int('AB2134', 13) + int('D8CCF', 17)))
'''

# Task 18

# наименьшее из 3 чисел: F4242(16), 3641101(8), 11110100001001000000(2). 
# В ответе запишите найденное наименьшее число в восьмеричной системе счисления.
'''

print(oct(min(int('F4242', 16), int('3641101', 8), int('11110100001001000000', 2))))
'''


# Task 19

# Example from Perplexity.ai
'''
def decimal_to_quinary(decimal):
    quinary = ''
    while decimal >= 5:
        quinary = str(decimal % 5) + quinary
        decimal //= 5
    quinary = str(decimal) + quinary
    return quinary

number = int(input())
quinary = decimal_to_quinary(number)
print(quinary)
'''


# Task 20

# Напишите программу, которая переведет введенное число в троичную систему счисления и 
# с помощью переменной-счетчик считает количество двоек в числе. 
# В качестве ответа программа выводит само число в троичной системе счисления и количество двоек через пробел

'''
'''
