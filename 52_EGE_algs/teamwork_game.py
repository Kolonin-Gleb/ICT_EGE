# Привет!
# Тест подключения! Видно?
# yes

# def isprime(n):
#     for i in range(1,n//2+1):
#         if n%i==0:
#             return False
#     return True

# for n in range(1,100):
#     s='>'+24*'4'+13*'5'+n*'6'

#     while ">4" in s or ">5" in s or ">6" in s:
#         if ">4" in s:
#             s = s.replace(">4", "15>", 1)
#         elif ">5" in s:
#             s = s.replace(">5", "23>", 1)
#         elif ">6" in s:
#             s = s.replace(">6", "7>", 1)
#     if isprime(sum([int(i) for i in range s])):
#         print(n)


# Как допишешь -- запускай и скажи Мише ответ!
# Преобразование числа по алгоритму
'''
for N in range(1,1000):
    N_2 = bin(N)[2:]
    N_2 = '1' + N_2 + str(N_2.count("1") % 2)

    N = int(N_2, 2)
    if N % 2 == 0:
        N_2 = N_2 + "1"
    else:
        N_2 = N_2 + "0"
    R = int(N_2, 2)
    if R < 320:
        print(R)
# 249
# :-(
# Не падать духом!
'''

# Теория Игр номер 7
'''
1 Куча

Ходы:
+1
*4
Победа при S >= 93

'''
"""
# 
def f(s, m): 
    if s >= 93: # усл. победы
        return m%2 == 0
    if m == 0: # ходы закончились
        return 0
    # Ещё есть ходы, что можно совершить
    h = [f(s+1,  m-1), f(s*4, m-1)]
    
    # Зазубрить эту формулу. Меняется лишь последняя часть?
    return any(h) if (m-1)%2 == 0 else all(h) 

print("20)", [s for s in range(1, 94) if not f(s, 2) and f(s, 4)]) # 21
"""

# *Негарантированная победа на 2 шаге, но гарантированная а 4от

# Рекурсия 7
'''
import sys
sys.setrecursionlimit(9999)

def F(n):
    if n == 1:
        return n
    return n - 1 + F(n - 1)

print(F(2434)-F(2430)) # 9726
'''

# Иполнитель 2
# Берём код выше!!!!

# def isprime(n):
#     for i in range(1,n//2+1):
#         if n%i==0:
#             return False
#     return True

# for n in range(1,100):
# s='2'+130*'8'

# while "18" in s or "288" in s or "3888" in s:
#     if "18" in s:
#         s = s.replace("18", "2", 1)
#     elif "288" in s:
#         s = s.replace("288", "7", 1)
#     elif "3888" in s:
#         s = s.replace("3888", "1", 1)

# print(s) #388

# ТИ 2
'''
def f(s, m): 
    if s >= 82: # усл. победы
        return m%2 == 0
    if m == 0: # ходы закончились
        return 0
    # Ещё есть ходы, что можно совершить
    h = [f(s+2,  m-1), f(s+4,  m-1), f(s*7, m-1)]
    
    # Зазубрить эту формулу. Меняется лишь последняя часть?
    return any(h) if (m-1)%2 == 0 else all(h) # all

print("Answer:", [s for s in range(1, 83) if not f(s, 1) and f(s, 7)]) # 922
'''

# Преобразование по алгоритму
'''
for N in range(99, 1000):
    N = str(N)
    a=(int(N[0])+int(N[1])) # 1ый + 2ой
    b=(int(N[1])+int(N[2])) # 2ый + 3ий
    # ЗАПУСКАЙЙЙЙЙЙ!!!!
    res = [a, b].sort(reverse=True)
    if res == 1613:
        print(N)
# Верным был 497
'''

'''
count = 0

for d1 in '135':
    for d2 in '0246':
        for d3 in '135':
            for d4 in '0246':
                for d5 in '135':
                    num = d1+d2+d3+d4+d5
                    if len(set(num)) == 5:
                        count += 1

for d1 in '246':
    for d2 in '135':
        for d3 in '0246':
            for d4 in '135':
                for d5 in '0246':
                    num = d1+d2+d3+d4+d5
                    if len(set(num)) == 5:
                    # Тут нужно было доп. проверки написать
                        count += 1


print(count) # 180
'''

# Рекурсия 4

# from functools import lru_cache
# import sys
# sys.setrecursionlimit(999)
# @lru_cache
# def F(n):
#     if n == 1:
#         return n
#     return n * F(n - 1)
# for i in range(1,3012):
#     F(i)
# print(F(3012)/F(3010)) # 

# Исполнитель 7
# (x \/ ¬y) /\ (y ≡ ¬z) /\ w.
# def f(n):
#     return int(bin(n)[2:]+'11'if n%2==0 else '1'+bin(n)[2:]+'01',2)
# for i in range (100001,0,-2):
#     if(f(i)<711):
#         print(f(i))
# for a in range(1,10**9):
#     if(a%10==0):
#         print(a)
#     flag=True
#     for x in range(1,10**7):
#         flag=False if((x%7==0) or ((20<=x<=55) <= (2*x + a >= 74)))==0 else flag
#     if flag:
#         print(a)
#         exit()