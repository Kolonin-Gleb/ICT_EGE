

# Task 5
'''
def dec_to_4(n):
    res = ''

    while n > 0:
        res = str(n % 4) + res
        n //= 4

    return res

for N in range(1, 1_001, 2):
    N_4 = dec_to_4(N)
    R_4 = ''

    if N % 3 == 0:
        first_dig = N_4[0]
        last_dig = N_4[-1]
        R_4 = last_dig + N_4[1:-1] + first_dig + '1'
    else:
        R_4 = N_4 + str(N % 3)

    R = int(R_4, 4)

    if R <= 340:
        print(R) # max => last R = 301
'''

# Task 13 IP
'''
from ipaddress import ip_network

counter = 0
for ip in ip_network('112.208.0.0/255.255.128.0', False):
    adr = bin(int(ip))[2:]
    if adr.count('1') % 11 == 0:
        counter += 1

print(counter) # 3003
'''

# Task 19-21 Game theory
"""
2 Кучи
a - 1 куча
b - 2 куча

Ходы:
+1
*2
Победа: (a + b) >= 59

Начальные кучи:
a = 5
1 <= b <= 53
"""

'''
def F(a, b, m):
    # победа
    if (a + b) >= 59:
        return m % 2 == 0
    # кончились ходы
    if m == 0:
        return 0
    # Все возможные ходы
    h = [F(a+1,b, m-1), F(a*2, b, m-1), F(a,b+1, m-1), F(a, b*2, m-1)]

    return any(h) if (m-1) % 2 == 0 else all(h) # неудачный ход => 2th all to any

# print("19)", [b for b in range(1, 54) if not F(5, b, 1) and F(5, b, 2)]) # minS = 14
# print("20)", [b for b in range(1, 54) if not F(5, b, 1) and F(5, b, 3)]) # 2 minS = 24 26
print("21)", [b for b in range(1, 54) if not F(5, b, 2) and F(5, b, 4)]) # minS = 23
'''

# Task 23
'''
def F(x, y, command):
    if x > y:
        return 0
    if x == y:
        return 1
    if command == 'a':
        return F(x+2, y, 'a') + F(x+3, y, 'b')
    return F(x+2, y, 'a') + F(x+3, y, 'b') + F(x*4, y, 'c')

print(F(1, 50, '-')) # 580143
'''

# Task 26 Excel
