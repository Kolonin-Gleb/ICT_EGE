
s = '3' * 70

while s.find('333') or s.find('888'):
    print(s)
    if s.find('333') != -1: # Если найдено
        s = s.replace('333', '8',1)
    else:
        s = s.replace('888', '3',1)

print("=========================")
print(s)
# Бесконечное выполнение - ответ 3383.