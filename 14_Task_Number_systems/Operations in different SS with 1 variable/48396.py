# https://inf-ege.sdamgia.ru/problem?id=48396

# 2x84(19) + 2B3x(16) % 88 min

for x in "0123456789ABCDEF":
    tmp = int('2' + x + '84', 19) + int('2B3' + x, 16)
    if tmp % 88 == 0:
        print(tmp // 88)
        break

# 345