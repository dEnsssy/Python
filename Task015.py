# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

from random import randint

list_1=[]

num=int(input('Введите количество оценок: '))

for i in range(num):
    list_1.append(randint(1,10))
print(f'Текущий: {list_1}', end="\n")

max1=max(list_1)
min1=min(list_1)
for i in range(len(list_1)):
    if list_1[i]==max1:
        list_1[i]=min1

print(list_1)

# from random import randint

# list_1=[]

# num=int(input('Введите количество оценок: '))
# for i in range(num):
#     list_1.append(randint(1,10))
# print(f'Текущий: {list_1}', end="\n")

# max1=max(list_1)
# for i in range(len(list_1)):
#     if list_1[i]==max1:
#         list_1[i]=1

# print(list_1)