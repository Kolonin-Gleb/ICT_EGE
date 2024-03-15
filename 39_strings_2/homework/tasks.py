# Task 1 # ТИП 17 в ЕГЭ

# Решение от Maximum (c моим разбором)
'''
f = open('homework/1.txt')
a = f.readline()
st = 'M' # минимальная цепочка вида MDVMDV
maxlen = 0 # длина максимальной найденной цепочки

while st in a: # пока цепочка есть в файле
    maxlen += 1
    # добавляем найденные символы в строку с учётом чередования MDV
    if st[-1] == 'M':
        st += 'D'
    elif st[-1] == 'D':
        st += 'V'
    else:
        st += 'M'
print(maxlen)
f.close()
'''

# Task 2
# Кол. строк в которых S > K на 9
'''
f = open('homework/2.txt')
counter = 0
lines = f.readlines()
for line in lines:
    if line.count("S") == (line.count("K") + 9):
        counter += 1

print(counter)
f.close()
'''

# Task 3
# Определите максимальную длину комбинации символов, удовлетворяющих маске T*F,
# где звёздочка обозначает любую последовательность символов, в том числе и пустую.
'''
file = open('homework/3.txt')
a = file.readline()
print(a.rfind('F') - a.find('T') + 1) # +1, т.к. find возращает индексы, а нам нужна длина
file.close()
'''

# Task 4
# My ideas
'''
file = open('homework/4.txt')
a = file.readline()

s = a[a.find('L'):a.rfind('G')+1] # Первичная выборка (от 1ой L до последней G)
print(s)

while a.count('L') != 1 and a.count('G') != 1:
    print("=============")
    s = a[a[1::].find('L'):a[-1::-1].rfind('G')]
    print(s)
    print("=============")
    break

print(len(s))
file.close()
'''

# ChatGPT
'''
text = open('homework/4.txt', 'r').read().strip()

max_length = 0
start = text.find('L')
while start != -1:
    end = text.rfind('G', start)
    if end != -1:
        max_length = max(max_length, end - start - 1)
        start = text.find('L', end)
    else:
        break

print("Максимальная длина комбинации L*G:", max_length) # 100373
'''

'''
text = open('homework/4.txt', 'r').read().strip()

max_length = 0
current_length = 0
for char in text:
    if char != 'L' and char != 'G':
        current_length += 1
    else:
        max_length = max(max_length, current_length)
        current_length = 0
max_length = max(max_length, current_length)

print("Максимальная длина комбинации L*G:", max_length)
'''

"""
def find_max_length_LG_sequence(text):
    max_length = 0
    current_length = 0
    inside_sequence = False

    for char in text:
        if char == 'L':
            inside_sequence = True
            current_length = 0
        elif char == 'G':
            if inside_sequence:
                max_length = max(max_length, current_length)
                inside_sequence = False
        else:
            if inside_sequence:
                current_length += 1

    return max_length

# Example usage:
# Assuming the text is read from a file or input
text = open('homework/4.txt', 'r').read().strip()
print(find_max_length_LG_sequence(text)) # Почти! Не 122, а 124!!!
"""

# Task 4
# Correct Maximum's solution
'''
file = open('homework/4.txt')
a = file.readline()
m = 0 # Длина максимальной последовательности
while a.count('L') > 0:
    a = a[a.find('L') + 1:] # Усекаем слева, пока имеются L
    rfi = a.find('G') # Самая первая G
    if a.find('L') > rfi:
        m = max(m, rfi + 2) # ПОЧЕМУ??? # +2, т.к. Работаем с индексами и границы не включаются при исп. find?

print(m)
file.close()
'''

# Task 5
# Определите количество строк, в которых встречается комбинация FI*SH
# где звёздочка обозначает любую последовательность символов, в том числе и пустую.
# NOT 9905
'''
file = open('homework/5.txt')
count = 0

for line in file:
    if (line.rfind('SH') - line.find('FI')) > 0 and line.find('FI') != -1 and line.rfind('SH') != -1:
        count += 1

print(count) # +1, т.к. find возращает индексы, а нам нужна длина

file.close()
'''

# Task 6
# Определите количество строк, в которых встречается комбинация MAX*AX,
# где звёздочка обозначает любую последовательность символов, в том числе и пустую.
'''
file = open('homework/6.txt')

count = 0
for line in file:
    if -1 < line.find('MAX') +2 < line.rfind('AX'):
        count += 1

print(count)
file.close()
'''

