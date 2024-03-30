# Task 9831

# Сколько существует шестнадцатеричных трёхзначных чисел,
# в которых все цифры различны и никакие две чётные или две нечётные цифры не стоят рядом?
# TODO: Насколько оптимально моё решение? Как сделать короче?
'''
counter = 0
for d1 in '123456789ABCDEF':
    for d2 in '0123456789ABCDEF':
        for d3 in '0123456789ABCDEF':
            s = d1+d2+d3
            # Все цифры различны
            if len(set(s)) == 3:
                # Чередование чётных и нечётных
                if (int(d1, 16) % 2 == 0 and int(d2, 16) % 2 != 0 and int(d3, 16) % 2 == 0) or (int(d1, 16) % 2 != 0 and int(d2, 16) % 2 == 0 and int(d3, 16) % 2 != 0):
                    counter += 1

print(counter) # 840
'''

# Task 9777
# Под каким номером в списке стоит
# последнее слово с нечётным номером,
# которое не начинается с буквы Ь и содержит ровно две буквы К?
'''
num = 0
letters = sorted('КОМПЬЮТЕР') # ВАЖНО ОБРАЩАТЬ ВНИМАНИЕ НЕ ТОЛЬКО НА ПРИВЕДЁННЫЙ ПРИМЕР СПИСКА, НО И НА БУКВЫ, ЧТО ИСПОЛЬЗУЮТСЯ ДЛЯ СОСТАВЛЕНИЯ СЛОВ.
# СПЕЦИАЛЬНО МОГУТ УПУСТИТЬ БУКВЫ В СПИСКЕ
# print(letters) # ['Е', 'К', 'М', 'О', 'П', 'Р', 'Т', 'Ь', 'Ю'] # Правильный порядок букв для перебора
for b1 in letters:
    for b2 in letters:
        for b3 in letters:
            for b4 in letters:
                for b5 in letters:
                    num += 1
                    s = b1 + b2 + b3 + b4 + b5
                    if (num % 2 != 0) and (b1 != 'Ь') and (s.count('К') == 2):
                        print(num, s)
# Answer: 58979
'''

# Task 9739
'''
num = 0
for b1 in sorted('МАНГУСТ'):
    for b2 in sorted('МАНГУСТ'):
        for b3 in sorted('МАНГУСТ'):
            for b4 in sorted('МАНГУСТ'):
                for b5 in sorted('МАНГУСТ'):
                    for b6 in sorted('МАНГУСТ'):
                        s = b1+b2+b3+b4+b5+b6
                        num += 1
                        if (b1 != "У") and (s.count('М') == 2) and (s.count("Г") <= 1):
                            print(num, s)
# Answer: 100810
'''

# Task 7587
'''
num = 0
for b1 in sorted('АВЛОР'):
    for b2 in sorted('АВЛОР'):
        for b3 in sorted('АВЛОР'):
            for b4 in sorted('АВЛОР'):
                num += 1
                s = b1+b2+b3+b4
                if b1 == "Л":
                    print(num)
                    exit()
'''

# Task 6894
'''
num = 0
for b1 in sorted("ЦАПЛЯ"):
    for b2 in sorted("ЦАПЛЯ"):
        for b3 in sorted("ЦАПЛЯ"):
            for b4 in sorted("ЦАПЛЯ"):
                for b5 in sorted("ЦАПЛЯ"):
                    num += 1
                    s = b1+b2+b3+b4+b5
                    if s.count("А") <= 1 and  s.count('Ц') == 2 and s.count("Л") == 0:
                        print(num, s)
                        exit()
'''

# Task 6892
'''
count = 0
for d1 in '12345':
    for d2 in '012345':
        for d3 in '012345':
            for d4 in '012345':
                for d5 in '012345':
                    for d6 in '012345':
                        s = d1+d2+d3+d4+d5+d6
                        if s.count('2') == 1:
                            ind_2 = s.find('2')
                            if (ind_2 == 0 and (int(s[1]) % 2 == 0)) or (ind_2 == 5 and (int(s[4]) % 2 == 0)):
                                count += 1
                            elif ( (int(s[ind_2 - 1]) % 2 == 0) and (int(s[ind_2 + 1]) % 2 == 0) ):
                                count += 1
print(count) # 3700
'''

# Task 6743
'''
num = 0
for b1 in sorted("СОЙКА"):
    for b2 in sorted("СОЙКА"):
        for b3 in sorted("СОЙКА"):
            for b4 in sorted("СОЙКА"):
                for b5 in sorted("СОЙКА"):
                    num += 1
                    s = b1+b2+b3+b4+b5
                    if s.count('О') <= 1:
                        no_2_C = True
                        for i in range(len(s) - 1):
                            if s[i] == s[i + 1] == "С":
                                no_2_C = False
                        if no_2_C:
                            print(num, s) # 2990
'''

# Task 6015
'''
count = 0
for d1 in '12345678':
    for d2 in '012345678':
        for d3 in '012345678':
            for d4 in '012345678':
                for d5 in '012345678':
                    for d6 in '012345678':
                        for d7 in '012345678':
                            s = d1+d2+d3+d4+d5+d6+d7
                            if s.count('8') == 1 and (int(s[0], 9) % 2 == 0) and (int(s[-1], 9) % 2 != 0):
                                count += 1

print(count) # 376832
'''


# Task 6040
# Чтобы проверить, что два числа имеют разную чётность (1 чётное, 2 нечётное)
# Сумма 2х чисел разной чётности будет НЕЧЁТНОЙ

# На будущее:
# Когда требуется выполнить сложную проверку (вроде чередования чётности)
# Её лучше вынести в отдельную функцию!
'''
count = 0
for d1 in '123456':
    for d2 in '0123456':
        for d3 in '0123456':
            for d4 in '0123456':
                for d5 in '0123456':
                    for d6 in '0123456':
                        s = d1+d2+d3+d4+d5+d6
                        if s.count('6') == 1:
                            even_odd_swaps = True
                            for i in range(len(s) - 1):
                                if (int(s[i], 7) + int(s[i + 1], 7)) % 2 == 0: # Если сумма чётна, то числа одной чётности!
                                    even_odd_swaps = False # такие не подходят
                                    break
                            if even_odd_swaps:
                                count += 1
print(count) # 1296
'''

# Task 5553
# Сколько можно составить различных кодов, в составе которых встречаются
# две подряд идущие гласные, путём перестановки букв слова СОТОЧКА?
# 7 Букв!
'''
count = 0
letters = set('СОТОЧКА')
for d1 in letters:
    for d2 in letters:
        for d3 in letters:
            for d4 in letters:
                for d5 in letters:
                    for d6 in letters:
                        for d7 in letters:
                            s = d1+d2+d3+d4+d5+d6+d7
                            # Образовано перестановкой
                            if s.count('О') == 2 and 'С' in s and 'Т' in s and 'Ч' in s and 'К' in s and 'А' in s:
                                # Есть 2 подряд гласные
                                if 'ОО' in s or 'ОА' in s or 'АО' in s:
                                    count += 1
print(count)
# ПОМНИ:
# Слова 
# ССССССО и ССССССО 
# Для нас одинаковые слова, а для питона он в конце взял первую О, а во втором случае вторую
# Для решение проблемы использовать set()
'''

# Task 4189
'''
num = 0
for b1 in sorted("БАТЫР"):
    for b2 in sorted("БАТЫР"):
        for b3 in sorted("БАТЫР"):
            for b4 in sorted("БАТЫР"):
                for b5 in sorted("БАТЫР"):
                    s = b1+b2+b3+b4+b5
                    num += 1
                    if s.count("Ы") == 0 and "АА" not in s:
                        print(num, s)
                        exit()
# 131
'''

