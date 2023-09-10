# https://inf-ege.sdamgia.ru/problem?id=48388

# x231y(12) + 78x98y(14) min % 99

search_results = []
for x in '0123456789AB':
    for y in '0123456789AB':
        tmp = int(x + '231' + y, 12) + int('78' + x + '98' + y, 14)

        if tmp % 99 == 0:
            search_results.append(tmp)

if search_results:
    print(min(search_results) // 99)

# 41428
