# https://inf-ege.sdamgia.ru/problem?id=48385
# 8x78y(13) + 79xy7(18)


serch_result = []

for x in '0123456789ABC':
    for y in '0123456789ABC':
        tmp = int('8' + x + '78' + y, 13) + int('79' + x + y + '7', 18)
        # Меньшая С.С. - 13, перебираем 13 значений

        if tmp % 9 == 0:
            serch_result.append(tmp)

if serch_result:
    print(min(serch_result) // 9)

# Answer = 113024
