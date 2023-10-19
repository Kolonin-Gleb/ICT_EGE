import random

str = 11 * '1' + 12 * '2' + 30 * '3'

lst = list(str)
random.shuffle(lst)

str = '>' + ''.join(lst)

while str.find('>1') or str.find('>2') or str.find('>3'):
    if str.find('>1') != -1:
        str = str.replace('>1', '22>', 1)
    if str.find('>2') != -1:
        str = str.replace('>2', '2>', 1)
    if str.find('>3') != -1:
        str = str.replace('>3', '1>', 1)
    if str[-1] == '>':
        break

print(str.count('2'))
