# https://inf-ege.sdamgia.ru/test?theme=274

# 90x4y(15) + 91xy2(16) % 56 min

serch_results = []

for x in '0123456789ABCDE':
    for y in '0123456789ABCDE':
        tmp = int("90" + x + "4" + y, 15) + int("91" + x + y + "2", 16)
        # Меньшая С.С. 15, перебираем 15 значений

        if tmp % 56 == 0:
            serch_results.append(tmp)

if serch_results:
    print(min(serch_results) // 56)

# 18754