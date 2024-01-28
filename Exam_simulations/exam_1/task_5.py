# Укажите наименьшее число N, после обработки которого с помощью данного алгоритма
# получается число R, большее 70.
# В ответе это число запишите в десятичной системе счисления.

R = 71

while True:
    print("R = ", R)
    bin_R = bin(R)
    # Забрать последние 2 бита
    last_2_sym = bin_R[-2:]
    bin_N = bin_R[:-2]

    # Восстановить 2 бита
    for _ in 1,2:
        if bin_N.count('1') % 2 == 1:
            bin_N += '1'
        else:
            bin_N += '0'

    # Совпало ли с ориганилом?
    # R_restored = int(bin_R, base=0)
    if bin_N == bin_R:
        N = int(bin_N[:-2],base=0)
        print(N)
        break
    else:
        R += 1

