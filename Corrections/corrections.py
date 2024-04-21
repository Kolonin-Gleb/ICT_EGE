# Logical functions

# Task 1
"""
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ( (x and (not y)) or (x == z) or (not w) ) == 0:
                    print(x, y, z, w)
"""
'''
x y z w
0 0 1 1
0 1 1 1
1 1 0 1
'''
# Answer: YZWX

# Task 2
"""
print("x y z")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            if ((x or y) <= (z == x)) == 0:
                print(x, y, z)
"""
# Answer: XZY

# Task 3
'''
print("x y z w")

for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if ( (not x) and (not y) or (y == z) or w ) == 0:
                    print(x, y, z, w)
'''

# Task 4
"""
"""

# Combinatorics
'''
# Task 1
counter = 0

for d1 in '24':
    for d2 in '13':
        for d3 in '024':
            for d4 in '13':
                for d5 in '024':
                    for d6 in '13':
                        counter += 1

for d1 in '13':
    for d2 in '024':
        for d3 in '13':
            for d4 in '024':
                for d5 in '13':
                    for d6 in '024':
                        counter += 1

print(counter)
'''

# Task 2
'''
counter = 0

for d1 in '2468':
    for d2 in '13579':
        for d3 in '02468':
            for d4 in '13579':
                for d5 in '02468':
                    for d6 in '13579':
                        num = d1+d2+d3+d4+d5+d6
                        if int(num) % 2 != 0 and len(set(num)) == 6:
                            counter += 1

for d1 in '13579':
    for d2 in '02468':
        for d3 in '13579':
            for d4 in '02468':
                for d5 in '13579':
                    for d6 in '02468':
                        num = d1+d2+d3+d4+d5+d6
                        if int(num) % 2 != 0 and len(set(num)) == 6:
                            counter += 1

print(counter)
'''

# Task 3
'''
counter = 0

for d1 in '123456':
    for d2 in '0123456':
        for d3 in '0123456':
            for d4 in '0123456':
                for d5 in '0123456':
                    num = d1+d2+d3+d4+d5
                    if num.count('3') == 1:
                        ind = num.find('3')
                        if ind == 0 and (int(num[1]) % 2 != 0):
                            counter += 1
                        elif ind == 4 and (int(num[3]) % 2 != 0):
                            counter += 1
                        elif int(num[ind - 1]) % 2 != 0 and int(num[ind + 1]) % 2 != 0:
                            counter += 1

print(counter)
'''

# Task 4
'''
counter = 0

for d1 in '1234567':
    for d2 in '01234567':
        for d3 in '01234567':
            for d4 in '01234567':
                for d5 in '01234567':
                    num = d1+d2+d3+d4+d5
                    if num.count('1') == 1:
                        ind = num.find('1')
                        if ind == 0 and (int(num[1]) % 2 == 0):
                            counter += 1
                        elif ind == 4 and (int(num[3]) % 2 == 0):
                            counter += 1
                        elif int(num[ind - 1]) % 2 == 0 and int(num[ind + 1]) % 2 == 0:
                            counter += 1

print(counter)
'''

# Task 5
'''
count = 0

for d1 in '12345678':
    for d2 in '012345678':
        for d3 in '012345678':
            for d4 in '012345678':
                for d5 in '012345678':
                    num = d1+d2+d3+d4+d5
                    if num.count('5') <= 1:
                        if num[-1] != '2' and num[-1] != '7':
                            if int(d1) % 2 == 0:
                                count += 1

print(count)
'''

# Task 6
'''
num = 0

for b1 in 'KOP':
    for b2 in 'KOP':
        for b3 in 'KOP':
            for b4 in 'KOP':
                for b5 in 'KOP':
                    num += 1
                    word = b1+b2+b3+b4+b5
                    if num == 190:
                        print(word)
                        exit() # РОКК
'''

# Task 7
'''
def check_different_letters(input_string):
    for i in range(len(input_string) - 2):
        if input_string[i] == input_string[i + 1] or input_string[i] == input_string[i + 2] or input_string[i + 1] == input_string[i + 2]:
            return False
    return True

num = 0

for b1 in "АИКР":
    for b2 in "АИКР":
        for b3 in "АИКР":
            for b4 in "АИКР":
                for b5 in "АИКР":
                    for b6 in "АИКР":
                        num += 1
                        word = b1+b2+b3+b4+b5+b6
                        if b1 == "И":
                            if check_different_letters(word):
                                print(num)
                                exit()
'''

# Task 8
'''
'''

