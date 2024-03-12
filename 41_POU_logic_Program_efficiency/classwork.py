# Эффективность программы
# Книга курса стр 100

# Task 1
#ind 0  1  2  3  4  5  6  7
'''
a = [1, 2, 3, 4, 5, 6, 7, 8]
for i in range(7): # range(7), т.к. по условию нельзя делать пару 88
    for j in range(i+1, 8):
        print(a[i], a[j])
'''

# Task 2
'''
f = open('2.txt')
N = int(f.readline())
a = [int(i) for i in f]
R = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if (a[i] + a[j]) % 2 != 0:
            R = max(R, a[i] + a[j])

print(R)
f.close()
'''


# Task 3
'''
f = open('3.txt')
N = int(f.readline())
a = [int(i) for i in f]

for i in range(N): # установка числа с которого начинаем суммировать
    s = 0 # Текущая временная сумма
    for j in range(i, N): # Выполнение суммирования
        s += a[j] # 
        print(s)

# print(R)
f.close()
'''
