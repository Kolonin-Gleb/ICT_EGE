# 1984
'''
counter = 0

for b1 in 'ИГРОК':
    for b2 in 'ИГРОК':
        for b3 in 'ИГРОК':
            for b4 in 'ИГРОК':
                for b5 in 'ИГРОК':
                    word = b1+b2+b3+b4+b5
                    if b1 != 'К' and len(set(word)) == 5 and 'РОК' not in word:
                        counter += 1

print(counter) #90
'''

# 1985
'''
counter = 0
for b1 in 'АБИКОЛУН':
    for b2 in 'АБИКОЛУН':
        for b3 in 'АБИКОЛУН':
            for b4 in 'АБИКОЛУН':
                for b5 in 'АБИКОЛУН':
                    for b6 in 'АБИКОЛУН':
                        for b7 in 'АБИКОЛУН':
                            for b8 in 'АБИКОЛУН':
                                word = b1+b2+b3+b4+b5+b6+b7+b8
                                if len(set(word)) == 8:
                                    word = word.replace('А', '1')
                                    word = word.replace('И', '1')
                                    word = word.replace('О', '1')
                                    word = word.replace('У', '1')
                                    word = word.replace('Б', '0')
                                    word = word.replace('К', '0')
                                    word = word.replace('Л', '0')
                                    word = word.replace('Н', '0')
                                    if '11' not in word and '00' not in word:
                                        counter += 1
print(counter) # 1152
'''

# 2350
'''
counter = 0
for b1 in '12346789':
    for b2 in '123456789':
        for b3 in '123456789':
            for b4 in '123456789':
                for b5 in '123456789':
                    for b6 in '123456789':
                        word = b1+b2+b3+b4+b5+b6
                        if word.count('2') == 2:
                            counter += 1
print(counter) # 56320
'''

# 2928
'''
counter = 0
for b1 in '1246':
    for b2 in '0123456':
        for b3 in '0123456':
            for b4 in '0123456':
                for b5 in '0123456':
                    for b6 in '0123456':
                        for b7 in '0123456':
                            code = b1+b2+b3+b4+b5+b6+b7
                            if not(code.count('22') != 0 and code.count('44') != 0):
                                counter += 1
print(counter) # 466456
'''

# 4320
'''
counter = 0
for b1 in '1234567':
    for b2 in '01234567':
        for b3 in '01234567':
            for b4 in '01234567':
                for b5 in '01234567':
                    for b6 in '01234567':
                            code = b1+b2+b3+b4+b5+b6
                            if int(code, 8) % 5 == 0 and len(set(code)) == 6: 
                                code = code.replace('0', 'e')
                                code = code.replace('2', 'e')
                                code = code.replace('4', 'e')
                                code = code.replace('6', 'e')
                                code = code.replace('1', 'o')
                                code = code.replace('3', 'o')
                                code = code.replace('5', 'o')
                                code = code.replace('7', 'o')
                                if not 'ee' in code and not 'oo' in code:
                                    counter += 1
print(counter) #208
'''

# 4957 # TODO: Почему неверно!!!?
'''
counter = 0

for b1 in set('АНАСТАСИЯ'):
    for b2 in set('АНАСТАСИЯ'):
        for b3 in set('АНАСТАСИЯ'):
            for b4 in set('АНАСТАСИЯ'):
                for b5 in set('АНАСТАСИЯ'):
                    for b6 in set('АНАСТАСИЯ'):
                        for b7 in set('АНАСТАСИЯ'):
                            for b8 in set('АНАСТАСИЯ'):
                                for b9 in set('АНАСТАСИЯ'):
                                    word = b1+b2+b3+b4+b5+b6+b7+b8+b9
                                    word = word.replace('А', '*')
                                    word = word.replace('Я', '*')
                                    word = word.replace('И', '*')
                                    word = word.replace('Н', '+')
                                    word = word.replace('С', '+')
                                    word = word.replace('Т', '+')
                                    if not('***' in word and '+++' in word):
                                        counter += 1

print(counter) # 8621154 - мой вывод
# 23040 - верный.
'''

# 5270
'''
'''

# 6080
'''
num = 0
nums = []
for b1 in sorted('КОФЕ'):
    for b2 in sorted('КОФЕ'):
        for b3 in sorted('КОФЕ'):
            for b4 in sorted('КОФЕ'):
                for b5 in sorted('КОФЕ'):
                    num += 1
                    word = b1+b2+b3+b4+b5
                    if (not 'ФО' in word and not "КО" in word and not "ОФ" in word and not "ОК" in word) and word.count('О') == 1:
                        nums.append(num)

print(nums[0] + nums[-1]) # 1014
'''

# 6743
'''
num = 0
for b1 in sorted('СОЙКА'):
    for b2 in sorted('СОЙКА'):
        for b3 in sorted('СОЙКА'):
            for b4 in sorted('СОЙКА'):
                for b5 in sorted('СОЙКА'):
                    num += 1
                    word = b1+b2+b3+b4+b5
                    if word.count('О') <= 1 and not "СС" in word:
                        print(num, word) # Последний = 2990 СОСКС
'''

# 7673
'''
num = 0
counter = 0
for b1 in sorted('XYZ203'):
    for b2 in sorted(set('XYZ203')):
        for b3 in sorted(set('XYZ203')):
            for b4 in sorted(set('XYZ203')):
                for b5 in sorted(set('XYZ203')):
                    for b6 in sorted(set('XYZ203')):
                        for b7 in sorted(set('XYZ203')):
                            num += 1
                            word = b1+b2+b3+b4+b5+b6+b7
                            print(num, word)
                            if num == 7:
                                exit() # Как бы настроить сортировочку?
'''

# 7994
'''
num = 0
words = []
for b1 in sorted('АКЛМНЯ'):
    for b2 in sorted(set('АКЛМНЯ')):
        for b3 in sorted(set('АКЛМНЯ')):
            for b4 in sorted(set('АКЛМНЯ')):
                for b5 in sorted(set('АКЛМНЯ')):
                    num += 1
                    word = b1+b2+b3+b4+b5
                    if word[:2] == "МН":
                        words.append(word)

print(len(words) - 2) #214
'''

