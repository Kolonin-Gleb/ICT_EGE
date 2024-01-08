# Solution example
# (¬ (x ∈ A) → (x ∈ P)) → ((x ∈ A) → (x ∈ Q))
# На числовой прямой даны два отрезка: P = [25; 50] и Q = [32; 47].
# Укажите НАИБОЛЬШУЮ возможную длину промежутка A, для которого формула
'''
P = [i for i in range(25, 51)]
Q = [i for i in range(32, 48)]
m = 0
for Amin in range(0, 60):
    for Amax in range(Amin + 1, 60):
        check = 1
        A = [i for i in range(Amin, Amax)]
        for x in range(0, 101):
            f = ((not(x in A)) <= (x in P)) <= ((x in A) <= (x in Q))
            if not f:
                check = 0
                break
        if check == 1:
            m = max(m,Amax - Amin)
print(m - 1)
'''
