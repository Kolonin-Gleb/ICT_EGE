import sys

sys.setrecursionlimit(10000)

def F(n):
    if n == 1:
        return 1
    elif n > 1:
        return n * F(n-1)

print(F(3056)//F(3052))
