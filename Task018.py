# Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива

from random import randint

list1=[]
list2=[]
result=[]
n=int(input('Введите количество элементов в первом списке: '))
m=int(input('Введите количество элементов во втором списке: '))
for i in range(n):
    list1.append(randint(1,20))
for i in range(m):
    list2.append(randint(1,20))

print(list1)
print(list2)

for i in range(len(list1)):
    if list1[i] not in list2:
        result.append(list1[i])

# result = [elem for elem in list1 if elem not in list2]

print(result)

