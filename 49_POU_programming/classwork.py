# Student's book Хакатон
# Task 2
'''
s = input()

if s[::1] == s[::-1]:
    print("Palindrome")
else:
    print("Bullshit!")
'''

# Task 3
# Python program to display the Fibonacci sequence
# a = [1, 1, sum of previous two]
# 15th number in sequence?
'''
def recur_fibo(n): # n-запрашиваемый эл. последовательности. Его номер.
    if n <= 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return (recur_fibo(n-1) + recur_fibo(n-2))

print(recur_fibo(15))
'''

# Task 4
'''
f = open("")
N = 100
a = []
for i in range(N+1):
    a.append(int(f.readline()))

a.sort(reverse=True)
print(int(a[19] - a[50]))
f.close()
'''

# Task 5
'''
f = open("24-s1.txt")
a = f.readline()
k = 0

for line in a:
    for i in range(len(line) - 8):
        if line[i] == 'A' and line[i + 1] == 'B' \
            and line[i + 3] == 'C' and line[i + 4] == 'X' \
                and line[i + 6] == 'Y' and line[i + 7] == 'Z':
            k += 1

print(k)
f.close()
'''

# Task 6
'''
prices = []

f = open("")
prices = f.readline().split()
m = 0
for i in range(len(prices)):
    for j in range(i, len(prices)):
        m = max(int(prices[j] - prices[i]), m)

prices(m)
'''

# POU Programming part 2
# Task 1
'''
f = open("")
a = f.readline()
a = a.replace("ACB", "*", 1)
a = a.replace("CAB", "*", 1)
m = 0 # тек. максимум
n = 0 # глоб. максимум

for sym in a:
    if sym == '*':
        n += 1
        m = max(n, m)
    else:
        n = 0
    print(m)


f.close()
'''


# Task 3
'''
# from fnmatch import fnmatch as shaman_stroka
# for i in range(0,10**9,1077):
#     if shaman_stroka(str(i),'183*9*7'):
#         print(i,i//1077)
'''



for i in range(18_397, 10**9, 1077):
    if i % 1077 == 0:
        start = i
        break

for i in range(start, 10**9, 1072):
    s = str(i)
    if s[:3] == '183' and s[-1] == '7' and "9" in s:
        pass

