# hw

'''
# Ex 2
lst = []
N = int(input())

for _ in range(N):
    lst.append(int(input()))

# print(sum(lst))
# for Ex 3

last = lst.pop()
counter = 0

for el in lst:
    if el < last:
        counter += 1

print(counter)
'''

# Ex 4

# lst = []
# N = int(input())

# max_3 = 0

# for _ in range(N):
#     tmp = int(input())
#     lst.append(tmp)
#     if tmp % 3 == 0 and tmp > max_3:
#         max_3 = tmp

# print(max_3)

# Ex 5
'''
def count_pairs_with_even(arr):
    count = 0
    n = len(arr)

    for i in range(n - 1):
        if arr[i] % 2 == 0 or arr[i + 1] % 2 == 0:
            count += 1

    return count

# Ввод данных
N = int(input("Введите количество элементов в массиве: "))
arr = []

for _ in range(N):
    arr.append(int(input()))

print(count_pairs_with_even(arr))
'''

# Ex 6
'''
def count_special_pairs(arr):
    count = 0
    n = len(arr)

    for i in range(n - 1):
        if (arr[i] % 2 == 0 and arr[i] % 5 == 0) and (arr[i + 1] % 2 == 0 and arr[i + 1] % 5 == 0):
            count += 1

    return count

# Ввод данных
N = int(input("Введите количество элементов в массиве: "))
arr = []

for _ in range(N):
    arr.append(int(input()))

print(count_special_pairs(arr))
'''

# Ex 6
'''
def count_special_pairs_2(arr, min_odd):
    count = 0
    n = len(arr)

    for i in range(n - 1):
        if (arr[i] % min_odd == 0 or arr[i + 1] % min_odd == 0):
            count += 1

    return count

N = int(input("Введите количество элементов в массиве: "))
arr = []
min_odd = 9999999999999999999999

for _ in range(N):
    tmp = int(input())
    arr.append(tmp)
    if tmp % 2 == 1:
        min_odd = min(min_odd, tmp)

print(count_special_pairs_2(arr, min_odd))
'''

# Task 8
'''
def count_special_triples(arr, max_5):
    count = 0
    n = len(arr)

    for i in range(n - 2):
        if (arr[i] % 6 == 0 and arr[i + 1] % 6 == 0 and arr[i + 2] % 6 == 0):
            if arr[i] * arr[i + 1] * arr[i + 2] >= max_5:
                count += 1

    return count

N = int(input("Введите количество элементов в массиве: "))
arr = []
max_5 = -9999999999999999999999

for _ in range(N):
    tmp = int(input())
    arr.append(tmp)
    if tmp % 5 == 0:
        max_5 = max(max_5, tmp)

print(count_special_triples(arr, max_5))
'''

