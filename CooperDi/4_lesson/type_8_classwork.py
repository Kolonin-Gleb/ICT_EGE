# 988 kompege.ru

# РЕШЕНИЕ КОДОМ!!!
# А не на бумаге с переводом С.С.
'''
k=0
for b1 in 'АИМРЯ':
    for b2 in 'АИМРЯ':
        for b3 in 'АИМРЯ':
            for b4 in 'АИМРЯ':
                s=b1+b2+b3+b4
                k+=1
                if s=='АРИЯ':
                    print(k) # 85
'''

# 9739
# Номер последнего
'''
k=0
for b1 in 'АГМНСТУ':
    for b2 in 'АГМНСТУ':
        for b3 in 'АГМНСТУ':
            for b4 in 'АГМНСТУ':
                for b5 in 'АГМНСТУ':
                    for b6 in 'АГМНСТУ':
                        s=b1+b2+b3+b4+b5+b6
                        k+=1
                        if b1!='У' and s.count('М')==2 and s.count('Г')<=1:
                            print(k,s)
'''

