# Task 1
'''
arr = [24, 32, 45, 126, 78, 56, 100]
print(sorted(arr, reverse=True))
'''

# Task 2
'''
with open("2.txt") as file:
    data = [int(i) for i in file]
    data = sorted(data)
    print(sum(data[:4]))
'''

# Task 3
'''
with open('3.txt') as file:
    data = [int(i) for i in file]
    m = max(data)
    print(abs(m - sum(data) / len(data)))
'''

# TODO: Переделать и перепроверить
# Task 4 
# Необходимо записать эти числа в массив и найти наибольшее количество элементов массива,
# сумма которых будет меньше 100;
'''
with open('4.txt') as file:
    data = [int(i) for i in file]
    N = data.pop(0)
    data = sorted(data) # по возрастанию

    s = 0
    for i in range(N):
        s += data[i]
        if s >= 100:
            print(i) # Возращаем i, т.к. индексация начинается с 0, поэтому -1 делать не нужно при нарушении условия
            # чтобы получить кол. чисел
            break
'''

# Task 5
# Cколько файлов наибольшего объёма можно сохранить в архиве.
'''
with open('5.txt') as file:
    S, N = map(int, file.readline().split())
    print(S, N)
    
    data = [int(i) for i in file]
    data = sorted(data, reverse=True) # descending
    
    s = 0
    for i in range(N):
        s += data[i]
        if s >= S:
            print(i) # Возращаем i, т.к. индексация начинается с 0, поэтому -1 делать не нужно при нарушении условия
            # чтобы получить кол. чисел
            break
'''

# Task 6
#  Определите максимальное число грузов, который может перевезти грузовик.
# N - кол. грузов
# M - грузоподъёмность (кг)
"""
with open('6.txt') as file:
    N, M = map(int, file.readline().split())

    data = [int(i) for i in file]
    data = sorted(data)

    m = 0
    for i in range(N):
        m += data[i]
        if m >= M:
            print(i) # Возращаем i, т.к. индексация начинается с 0, поэтому -1 делать не нужно при нарушении условия
            # чтобы получить кол. чисел
            break
"""
