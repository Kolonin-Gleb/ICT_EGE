

# Определите максимальное количество идущих подряд символов,
# среди которых никакие две гласные и никакие две согласные буквы не стоят рядом.

# M, A, X, I, U

# Подсмотрев в файл понимаю, что начинается с согласного X
'''
soglasniy = "MX" # 0
glasniy = 'AIU'  # 1

with open('24.txt') as file:
    data = file.readline()
    Max = 0

    flag = 0
    current_swap_len = 1
    
    for el in data[1::]:
        if el in glasniy and flag == 0:
            current_swap_len += 1
            flag = 1
        elif el in soglasniy and flag == 1:
            current_swap_len += 1
            flag = 0
        else:
            Max = max(Max, current_swap_len)
            current_swap_len = 1

    print(Max)
'''
