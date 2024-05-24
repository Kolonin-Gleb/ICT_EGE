# 0) Определить решаем Excel или Python
# Задача на очередь в камеру хранения => Python
# Проверить отсортированы ли числа в предоставлеенном файле!!!
# 1) Разобрать принцип алгоритма используя пример и ответ к нему.
'''
f = open("26_7626.txt")
# f = open("exmple_7626.txt")
K = int(f.readline()) # Кол. ячеек.
N = int(f.readline()) # Кол. пассажиров.
queue = [] # очередь
vault = [0] * K

for i in range(N):
    st, end = map(int, f.readline().split())
    queue.append([st, end])

queue.sort() # Правильно выстроенная очередь пассажиров
# print(queue)

left_luggage = 0 # кол. оставивших багаж
last_placed_num = 0 # Номер ячейки в которую в последнюю положили багаж

for passanger in queue:
    for vault_index in range(K):
        if vault[vault_index] < passanger[0]:
            vault[vault_index] = passanger[1]
            left_luggage += 1
            last_placed_num = vault_index + 1
            break # Пассажир пложивший багаж ушёл

f.close()
print(left_luggage, last_placed_num) # 581 59
'''

# Code by CooperDi
'''
f=open('26_7626.txt')

k=int(f.readline()) #кол-во ячеек
n=int(f.readline()) #кол-во пассажиров
a=[]
for i in range(n):
    st,end=map(int,f.readline().split())
    a.append([st,end])
a.sort()

camera=[0]*k #кол-во ячеек
count=0 #кол-во человек, которые сдали багаж
last=0 #номер ячейки, куда положили последний багаж
for i in range(n):
    st,end=a[i]
    for j in range(k):
        if camera[j]<st:
            camera[j]=end
            count+=1
            last=j+1
            break
print(count,last)
'''
