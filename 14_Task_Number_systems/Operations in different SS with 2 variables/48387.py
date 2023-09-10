# https://inf-ege.sdamgia.ru/problem?id=48387

# x341y(11) + 56x1y(19)
# При каких x и y min % 305 ?


serch_results = []

for x in '0123456789A':
    for y in '0123456789A':
        tmp = int(x + '341' + y, 11) + int('56' + x + '1' + y, 19)
        # Меньшая С.С. 11, перебираем 11 значений

        if tmp % 305 == 0:
            serch_results.append(tmp)

if serch_results:
    print(min(serch_results) // 305)

# Answer 2778