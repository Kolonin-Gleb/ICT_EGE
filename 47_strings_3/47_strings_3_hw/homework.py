# Обработка строк ч.3

# Task 1
'''
f = open('1.txt')
line = f.readline()
line = line.replace('XY', '*').replace("XZ", "*")
f.close()

k = 1 # тек. макс. последовательность.
m = 1 # глоб. макс. последовательность.
for i in range(len(line) - 1):
    if line[i] == line[i + 1] and line[i] == '*':
        k += 1
    else:
        m = max(m, k)
        k = 1
print(m)
'''

# Task 2
'''
f = open('2.txt')
line = f.readline()
# Разделим последовательность QO b OQ пробелами.
# Таким образом в строке последовательности символов, где нет соседствующих Q и O будут разделены пробелом
line = line.replace('QO', 'Q O').replace("OQ", "O Q")
data = line.split()
f.close()

mmax = 0 # глоб. макс. последовательность.
for seq in data:
    mmax = max(len(seq), mmax)

print(mmax)
'''

# Task 3
'''
f = open('3.txt')
lines = f.readlines()
f.close()

counter = 0
for line in lines:
    if "PLOV" in line:
        counter += 1

print(counter)
'''

# Task 4
'''
f = open('4.txt')
lines = f.readlines()
f.close()

counter = 0

# for line in lines:
#     ind_1 = line.find("SUP")
#     ind_2 = line[ind_1+1:].find("SUP")
#     ind_3 = line[ind_2+1:].find("SUP")
#     ind_4 = line[ind_3+1:].find("SUP")

#     if ind_1 != -1 and ind_2 != -1 and ind_3 != -1 and ind_4 == -1:
#         counter += 1

for line in lines:
    if line.count("SUP") == 3:
        counter += 1

print(counter)
'''
