# На вход подается число a. Напишите программу, которая уменьшает это число на 7,
# пока это число нечетное или больше 100, затем выводит полученное число на экран.
'''
a = int(input())

while a % 2 == 1 or a > 100:
    a -= 7
    print(a)
'''

# На вход подается на первой строке натуральное число n, затем на следующих n строках n целых чисел.
# Напишите программу, которая считает сумму введенных чисел, затем выводит ее на экран.

'''
n = int(input())
s = 0
for _ in range(n):
    s += int(input())

print(s)
'''

# Task 5
'''
n = int(input())
s = 0
for _ in range(n):
    s += int(input())

if s % 2 == 0:
    print(s)
else:
    print(2 * s)
'''

# Task 6
'''
n = int(input())
s_pos = 0
s_neg = 0
for _ in range(n):
    tmp = int(input())

    if tmp > 0:
        s_pos += tmp
    else:
        s_neg += tmp

print(s_pos, s_neg)
'''

# Task 7
'''
counter = 0
for i in range(10000, 100001, 1):
    if i % 3 == 0 and i % 9 != 0:
        counter += 1

print(counter)
'''

# 
