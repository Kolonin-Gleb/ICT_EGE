# Сколько единиц содержится в двоичной записи значения выражения:
# 8^2020 + 4^2017 + 26 – 1?'

res = 8 ** 2020 + 4 ** 2017 + 26 - 1
res = bin(res)
print(res[2:].count('1'))