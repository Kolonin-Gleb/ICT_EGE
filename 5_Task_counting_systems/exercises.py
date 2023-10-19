# Task 19
# Перевод из 10ой в 5ую С.С.
'''
# Из 10 С.С. в 5 С.С.
def decimal_to_res_count_system(decimal_num, res_count_system):
    if decimal_num == 0:
        return "0"

    count_system_num = ""
    while decimal_num > 0:
        ostatok = decimal_num % res_count_system
        count_system_num = str(ostatok) + count_system_num
        decimal_num = decimal_num // res_count_system

    return count_system_num

# Ввод числа
decimal_number = int(input("Введите десятичное число: "))

# Перевод в _ систему
res_count_system = 5

# Запуск перевода
result = decimal_to_res_count_system(decimal_number, )

# Число в пятеричной системе:
print(result)
'''


# Task 20
# Перевод из 10ой в 3ую С.С.
# Подсчёт 2ек в результате
'''
'''

# Из 10 С.С. в 5 С.С.
def decimal_to_res_count_system(decimal_num, res_count_system):
    if decimal_num == 0:
        return "0"

    count_system_num = ""
    while decimal_num > 0:
        ostatok = decimal_num % res_count_system
        count_system_num = str(ostatok) + count_system_num
        decimal_num = decimal_num // res_count_system

    return count_system_num

# Ввод числа
decimal_number = int(input("Введите десятичное число: "))

# Перевод в _ систему
res_count_system = 3

# Запуск перевода
result = decimal_to_res_count_system(decimal_number, res_count_system)

# Результат и Количество 2ек
print(result, result.count("2"))
