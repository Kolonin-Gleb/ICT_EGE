
# Task 2
'''
with open('1.txt', 'r') as file_txt:
    lst = file_txt.readlines()
    print(*lst, sep='')
'''

# Task 3
'''
with open('3.txt', 'r') as file_txt:
    lst = file_txt.readlines()
    odd_count = 0
    for num in lst:
        if int(num[:-1]) % 2 == 1:
            odd_count += 1
    print(odd_count)
'''

# Task 4
'''
with open('4.txt', 'r') as file_txt:
    lst = file_txt.readlines()
    count = 0
    for num in lst:
        if int(num[:-1]) % 10 == 7:
            count += 1
    print(count)
'''

# Task 5
'''
with open('5.txt', 'r') as file_txt:
    lst = file_txt.readlines()
    res = 1
    for num in lst:
        if int(num[:-1]) % 5 == 0:
            res *= int(num[:-1])
    print(res)
'''

# Task 6
# среднее арифметическое чисел, хранящихся в файле «6.txt». Обратите внимание,
# что в каждой строчке находится по одному числу. В ответ укажите только целое число.
'''
with open('6.txt', 'r') as file_txt:
    lst = file_txt.readlines()
    mean_avg = 0
    for num in lst:
        mean_avg += int(num[:-1])
    mean_avg = mean_avg / len(lst)
    print(mean_avg)
# 473
'''

# Task 7
'''
# по возрастанию
with open('7.txt', 'r') as file_txt:
    lst = file_txt.readlines()
    lst = [int(num) for num in lst]
    print(min(lst), max(lst))
'''

# Task 8
# Beautiful isn't it?
# Похоже на 17 номер в ЕГЭ
'''
with open('8.txt', 'r') as file_txt:
    sum = 0
    lst = file_txt.readlines()
    for pair in lst:
        m = min(map(int, pair[:-1].split(' ')))
        if m % 3 == 0:
            sum += m

    print(sum)
'''

# Task 9
# максимальный элемент и накопит произведение всех найденных максимальных элементов пар,
# хранящихся в файле. В ответ запишите первые 5 цифр полученного значения.
'''
'''

# 1015 - taken out of the file
# 56195 - wrong?!
with open('8.txt', 'r') as file_txt:
    mul = 1
    lst = file_txt.readlines()
    for pair in lst:
        m = max(map(int, pair[:-1].split(' ')))
        mul *= m

    print(mul)