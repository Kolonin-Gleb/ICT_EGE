# https://inf-ege.sdamgia.ru/problem?id=48394


# 4Cx4(15) + x62A(13) min % 121

for x in '0123456789ABC':
    tmp = int("4C" + x + "4", 15) + int(x + "62" + "A", 13)
    if tmp % 121 == 0:
        print(tmp // 121)
        break

#  234