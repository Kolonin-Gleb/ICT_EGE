# Task 7
'''
arr = [1, 2, 3, 50_000] 
N = len(arr)

min_14 = 14_000_000

for el in arr:
    if el % 14 and el < min_14:
        min_14 = el

count = 0
max_pair = 0
for i in range(len(arr) - 1):
    if all(arr[i] % min_14 == 0 and arr[i + 1] % min_14 == 0):
        count += 1
        max_pair = max(arr[i] + arr[i + 1], max_pair)

print(count, max_pair)
'''
