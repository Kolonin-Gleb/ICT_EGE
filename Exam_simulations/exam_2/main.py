# Task 2
'''
print("x, y, z, w")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if ( x and not(y) and (z <= w) ) == 1:
                    print(x, y, z, w)
# xywz
'''

# Task 5
'''
for N in range(1, 101):
    bin_N = bin(N)[2:]
    if bin_N.count('1') % 2 == 0:
        bin_R = '10' + bin_N[2:] + '0'
    else:
        bin_R = '11' + bin_N[2:] + '1'
    
    R = int(bin_R, 2)
    if R > 61:
        print(N)
        break
# 31
'''

# Task 9
'''
import csv
with open('9.csv', 'r') as f:
    row_values = f.readline()[:-1].split(';')
    print(row_values)
'''

# Task 16
'''
def F(n):
    if n < 3:
        return n
    if n >= 3:
        return F(n - 1) + F(n - 3)

print(F(18)) #683
'''

# Task 19
'''
'''

# Task 23
# ДОЛЖНО СОДЕРЖАТЬ 10
'''
def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    else:
        return f(x + 1, y) + f(x + 2, y) + f(x * 2, y)
print(f(3, 10) * f(10, 12))
'''
# 21 - неверно!
# 60 - верно

# Task 24
'''
'''
