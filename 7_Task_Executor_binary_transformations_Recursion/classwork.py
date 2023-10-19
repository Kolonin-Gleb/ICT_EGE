# def F(n):
#     if n <= 4:
#         return 2 * n
#     if n < 9:
#         return F(n-1) + 3
#     else:
#         return F(n - 3) + 5 + F(n -1)

# print(F(28))

# def F(n):
#     if n <= 2:
#         return 3 * n + 6
#     if n > 2 and n % 2 == 0:
#         return F(n-2) + 2 * F(n-1)
#     else:
#         return 10 + F(n - 4)

# print(F(18))


# import sys
# sys.setrecursionlimit(999999)

for n in range (1,100):
    s = bin(n)[2:]
    if s.count('1') % 2 == 0:
        s += '00'
    else:
        s += '10'
    r = int(s,2) # Возврат в 10 С.С.
    if r>52:
        print(r)
        break

