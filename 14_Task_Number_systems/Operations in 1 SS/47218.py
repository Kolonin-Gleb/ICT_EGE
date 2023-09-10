# https://inf-ege.sdamgia.ru/problem?id=47218

# 123x5(15) + 1x233(15) % 14 min

for x in '0123456789ABCDE':
    tmp = int('123' + x + '5', 15) + int('1' + x + '233', 15)
    if tmp % 14 == 0:
        print(tmp // 14)
        break

# 8767
