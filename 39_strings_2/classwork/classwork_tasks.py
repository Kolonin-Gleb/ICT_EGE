# Обработка строк 2.
# 24 номер в ЕГЭ

# Task 1
'''
1. Открываем файл
2. Считываем данные из файла
3. Объявляем пер. для текущей и максимальной длины подстроки
4. Анализируем считанную строку
'''
# Максимальная длина KL or LK
"""
f = open('24_1.txt')
line = f.readline() # 
k = 1
m = 1 # Максимальная найденная


for i in range(len(line) - 1):
    if line[i] == 'K' and line[i + 1] == 'L':
        k+=1
        m = max(k, m)
    elif line[i] == 'L' and line[i + 1] == 'K': # 2
        k += 1
        m = max(k, m)
    else: # Если последовательность оборвалась
        k = 1
print(m)
f.close() # 
"""

# Task 2
"""
f = open('24_2.txt')
lines = f.readlines()
k = 0
for line in lines:
    if line.count("K") > line.count("L"):
        k += 1
print(k)
f.close() # 552
"""

# Task 3
# 10^6 заглавных латинских букв
# Текст разбит на строки различной длины
# AB*YZ

# Найти кол. строк, в которых встречается комбинация AB*YZ
# где * обозначает любую последовательность символов, в том числе и пустую.
'''
f = open('24_3.txt')
lines = f.readlines()
k = 0
for line in lines:
    if line.find("AB") < line.rfind("YZ") and "AB" in line and "YZ" in line: # проверка and YZ символична
        k += 1
print(k)
f.close() # 144
'''

# Task 4
'''
f = open("24_4.txt")
s = f.readline().replace("BC", "*").replace("AC", "*")
k = "*"
m = 0

while k in s:
    k += "*"
    m = max(len(k), m)
print(m)
f.close()
'''

# Task 5
'''
f = open("")
s = f.readline().replace("XZ", "X Z").replace("ZX", "Z X")
s = s.split()
m = max([len(i) for i in s])
print(m)
f.close()
'''

# Task 6
'''
'''

