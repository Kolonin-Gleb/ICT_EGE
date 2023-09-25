
for x in reversed('0123456789ABCDEF'):
    Arithmetic = (int(x+'AD'+x+x, 16) - int('4'+x+'32', 16))
    if Arithmetic % 9 == 0:
        res = (int(x+'AD'+x+x, 16) - int('4'+x+'32', 16)) / 9
        break

print(res)