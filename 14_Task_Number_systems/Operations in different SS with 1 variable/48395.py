# https://inf-ege.sdamgia.ru/problem?id=48395

# 28x2(18) + 93x5(12) % 133 min

for x in "0123456789AB":
    tmp = int('28' + x + '2', 18) + int('93' + x + '5', 12)
    if tmp % 133 == 0:
        print(tmp // 133)
        break
