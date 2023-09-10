# https://inf-ege.sdamgia.ru/problem?id=48389

# yx320(7) + 1x3y3(9) min % 181

search_results = []

for x in '0123456':
    for y in '0123456':
        tmp = int(y + x + "320", 7) + int("1" + x + "3" + y + "3", 9)

    if tmp % 181 == 0:
        search_results.append(tmp)

if search_results:
    print(min(search_results) // 181)

# 148