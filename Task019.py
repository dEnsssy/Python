# Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

from random import randint
# list_0=[]
# m=int(input("Введите длину: "))
# for i in range(m):
#     list_0.append(randint(0,15))
# n = 0
# for i in range(1,len(list_0) - 1):
#     if list_0[i-1] < list_0[i ] > list_0[i + 1]:
#         n = n + 1
# print(list_0)
# print(n)

print(list_1:=[randint(0,15) for _ in range(int(input("Введите длину:")))])

print(len([0 for i in range(1,len(list_1)-1) if list_1[i-1] < list_1[i ] > list_1[i + 1]]))