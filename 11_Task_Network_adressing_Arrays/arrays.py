# Task 1
'''
A = [5, 14, -3, 8, -9, 0, 0, 7, -3, 20]

s = 0
for i in range(7):
    s = A[i]

print(s)
'''

# Task 5
'''
A = [2, 11, -9, 8, 4, 3, -3, 8, -5, -10]

s = 1
for j in range(10):
    if A[j] <= A[2] // 3:
        s = s*j

print(s)
'''

# Task 6
'''
lst = []

for i in range(5):
    lst.append(int(input()))

max_multiplicited_3 = -999

for el in lst:
    if el % 3 == 0 and el > max_multiplicited_3:
        max_multiplicited_3 = el

print(max_multiplicited_3)
'''

# Task 7
'''
count = int(input())
lst = []

# Т.к. вводятся лишь натуральные числа можно задать изначальное значение -1
# Позволит удобно обрабатывать случай, когда чисел оканчивающихся на 2 не было
ends_with_2_product = -1

for _ in range(count):
    el = input()
    if el[-1] == '2':
        ends_with_2_product *= int(el)
    lst.append(int(el))

if ends_with_2_product == -1:
    print("0")
else:
    print(ends_with_2_product*-1)
'''

# Task 8
'''
# Ах, да. В моей хитрой реализации не хватает добпвления элементов в массив.
# Исправим =)
N = int(input())
counter = 0
lst = []

for _ in range(N):
    el = int(input())
    if el % 2 == 0 and el > 5:
        counter += 1
    lst.append(el)

print(counter)
'''

# Task 9
'''
N = int(input())

sum_of_indexes_pos_elements = 0
lst = []

for i in range(N):
    el = int(input())
    lst.append(el)

    if el > 0 and el % 7 == 0:
        sum_of_indexes_pos_elements += i

print(sum_of_indexes_pos_elements)
'''
